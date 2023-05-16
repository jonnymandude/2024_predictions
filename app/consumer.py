from confluent_kafka import Consumer
from kafka_utils import read_ccloud_config
from data import MarketData
import ast
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


props = read_ccloud_config("secrets/client.properties")
props["group.id"] = "python-group-1"
props["auto.offset.reset"] = "earliest"

consumer = Consumer(props)
consumer.subscribe(["pres_predictions"])

conn_str = os.getenv('CONN_STR')
engine = create_engine(conn_str)
connection = engine.connect()
db_session = scoped_session(sessionmaker(bind=engine))


try:
    while True:
        msg = consumer.poll(1.0)
        print(msg)
        if msg is not None and msg.error() is None:
            print("Topic Name=%s, Message=%s"%(msg.topic,msg.value))
            print("key = {key:12} value = {value:12}".format(key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
            values = msg.value().decode('utf-8')
            values_dict = ast.literal_eval(values)


            # See if an observation exists
            obj_exists = db_session.query(MarketData.data_id).filter_by(data_id=values_dict['id'], timestamp=values_dict['timestamp']).first() is not None

            if not obj_exists: 
                # Create the new data
                newData = MarketData(
                    data_id=values_dict['id'],
                    name = values_dict['name'],
                    image = values_dict['image'],
                    market_image = values_dict['market_image'],
                    price = values_dict['price'],
                    buy = values_dict['buy'],
                    sell = values_dict['sell'],
                    timestamp = values_dict['timestamp'],
                    market_id = values_dict['market_id'],
                    market_name = values_dict['market_name'],
                )

                # Add in the new data models
                db_session.add(newData)
                db_session.commit()
            

except KeyboardInterrupt:
    pass
finally:
    consumer.close()