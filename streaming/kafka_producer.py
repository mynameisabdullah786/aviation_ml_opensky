from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

flight_data = {
    "altitude":30000,
    "velocity":450,
    "heading":180
}

producer.send("flight_stream",flight_data)