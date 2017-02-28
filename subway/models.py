from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, MetaData, ForeignKey, Text, Float
from sqlalchemy.orm import mapper
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()



class Station(Base):
    """
    A subway station, like "Atlantic - Pacific"
    """
    __tablename__ = 'stations'


    id = Column(Integer, primary_key=True)
    sid = Column(String)
    name = Column(String)
    lat = Column(Float)
    lng = Column(Float)

    def __init__(self, sid, name, lat, lng):
        self.sid = sid
        self.name = name
        self.lat = lat
        self.lng = lng


class SubStation(Base):
    """
    A subway substation, like 116N [116th Street North]
    """
    __tablename__ = 'substations'

    id = Column(Integer, primary_key=True)
    pid = Column(Integer, ForeignKey('stations.id'))
    name = Column(String)


class Route(Base):
    """
    A subway route like 1 or D.
    """
    __tablename__ = 'routes'

    id = Column(Integer, primary_key=True)
    rid = Column(String)
    name = Column(String)
    description = Column(String)
    color = Column(String)

    def __init__(self, rid, name, description, color):
        self.rid = rid
        self.name = name
        self.description = description
        self.color = color



Base.metadata.create_all(engine)
