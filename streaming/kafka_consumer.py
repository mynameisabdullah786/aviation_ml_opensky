from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "flight_stream",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

for msg in consumer:

    flight = msg.value

    print("Received flight data:",flight)