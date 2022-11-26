##### KAFKA #####
# Go inside Kafka container instance
docker exec -it eft-kafka-1 bash

# Go to Kafka bin directory
cd /opt/bitnami/kafka

# List Topics
bin/kafka-topics.sh --list --bootstrap-server localhost:9092

# Create Topics
bin/kafka-topics.sh --create --topic ecommerce.tracker --bootstrap-server localhost:9092

# Producer (Sample)
bin/kafka-console-producer.sh --topic ecommerce.tracker --bootstrap-server localhost:9092

# Consumer (Sample)
bin/kafka-console-consumer.sh --topic ecommerce.tracker --from-beginning --bootstrap-server localhost:9092