from confluent_kafka import Consumer
from kafka_utils import read_ccloud_config

props = read_ccloud_config("../secrets/client.properties")
props["group.id"] = "python-group-1"
props["auto.offset.reset"] = "earliest"

consumer = Consumer(props)
consumer.subscribe(["pres_predictions"])


try:
    while True:
        msg = consumer.poll(1.0)
        print(msg)
        if msg is not None:
            print(msg.error())
            print("Topic Name=%s, Message=%s"%(msg.topic,msg.value))
            print("key = {key:12} value = {value:12}".format(key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
except KeyboardInterrupt:
    pass
finally:
    consumer.close()