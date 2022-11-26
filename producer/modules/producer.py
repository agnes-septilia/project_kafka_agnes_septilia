import logging

import threading
import time
import json
from datetime import datetime
from random import SystemRandom
from kafka import KafkaProducer

from modules import funnel


class ProducerThread(threading.Thread):
    """
    Producer in Thread

    Producer function that run in single thread, allowing multithread runtime.
    Inherited from Thread.

    params:
    - name: str. Thread process name (label).
    - args: tuple. Arguments used by producer function.
    - topic: str. Topic for producer to publish data.
    """
    def __init__(self, name: str, args: tuple, bootstrap_servers: str, topic: str):
        super().__init__(
            target = self._produce,
            name   = name,
            args   = args
        )
        self.active = False
        
        self._setup_publisher(bootstrap_servers, topic)
        self.logger = logging.getLogger(__name__)


    # Public Methods
    def start(self):
        """
        Start Thread

        Starting thread activity by setting object active state to True
        """
        self.active = True
        super().start()

    def stop(self):
        """"
        Stop Thread

        Stopping Thread activity by setting object active state to False.
        """
        self.active = False


    # Private Methods
    def _setup_publisher(self, bootstrap_servers, topic):
        kafka_logger = logging.getLogger("kafka.conn")
        kafka_logger.setLevel(logging.ERROR)
        
        self.publisher = KafkaProducer(
            value_serializer = lambda d: json.dumps(d).encode("utf-8"),
            bootstrap_servers = bootstrap_servers
        )
        self.topic = topic

    def _produce(self, id: int):
        while (self.active):
            user_id    = SystemRandom().randint(0, 300)
            session_id = f"{datetime.now():%Y%m%d%H%M%S}_{user_id}"
   
            self.logger.info(f"Producer {id:2}: Create data with Session '{session_id}'")
            event_list = funnel.generate_random_funnel(user_id, session_id)
            for event in event_list:
                self._publish({**event, "event_timestamp": round(datetime.now().timestamp())})
                time.sleep(2 + (3 * SystemRandom().random()))
            time.sleep(3)

    def _publish(self, data: dict):
        future = self.publisher.send(self.topic, data)
        future.get(timeout = 5)