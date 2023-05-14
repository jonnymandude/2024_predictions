from confluent_kafka import Producer
from kafka_utils import read_ccloud_config

producer = Producer(read_ccloud_config("../secrets/client.properties"))
producer.produce("pres_predictions", key="key", value="value")
