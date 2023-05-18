from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
import os

Base = declarative_base()

class MarketData(Base):
    __tablename__ = "market_data"
    data_id = Column(Integer, primary_key=True)
    name = Column(String(250))
    image = Column(String(250))
    market_image = Column(String(250))
    price = Column(Float)
    buy = Column(Float)
    sell = Column(Float)
    timestamp = Column(DateTime(timezone=False), primary_key=True)
    market_id = Column(Integer)
    market_name = Column(String(250))


    def __repr__(self):
        return "<MarketData(name='%s', market_name='%s', price='%s')>" % (
            self.name,
            self.market_name,
            self.price,
        )

if __name__ == '__main__':
    conn_str = os.getenv('CONN_STR')
    engine = create_engine(conn_str)
    Base.metadata.create_all(engine)