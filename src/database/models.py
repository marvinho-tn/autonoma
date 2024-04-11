from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    value = Column(String)
    timestamp = Column(DateTime, default=func.now())
    source_id = Column(Integer, ForeignKey('source.id'))
    source = relationship('Source')

class Source(Base):
    __tablename__ = 'source'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    data = relationship('Data')