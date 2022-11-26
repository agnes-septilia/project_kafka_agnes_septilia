""" NOTE TO MENTOR
Karena program selalu gagal setiap dijalankan dengan docker, 
maka script ini dibuat dengan dijalankan tanpa docker
"""


import json
from kafka import KafkaConsumer
from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres:1234@localhost:5432")

consumer = KafkaConsumer(
    "ecommerce.tracker",
    # auto_offset_reset = "earliest",
    bootstrap_servers = ["localhost:9092"],
    value_deserializer = lambda m: json.loads(m.decode("utf-8"))
)

for message in consumer:
    # print(message.value)
    with open("consumer/result.json", "a") as file:
        file.write(json.dumps(message.value))
        file.write("\n")

    json_data = message.value
    event = {
        "page_type": json_data["core"]["page_type"],    # page_type
        "page_url": json_data["core"]["page_url"],  # page_url
        "user_id": json_data["user"]["user_id"],   # user_id
        "session_id": json_data["user"]["session_id"],  # session_id
        "event_timestamp": json_data["event_timestamp"]    # event_timestamp
    }

    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO project6.events VALUES (:page_type, :page_url, :user_id, :session_id, :event_timestamp)"),
            [event]
        )