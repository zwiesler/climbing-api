from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, func, Float

Base = declarative_base()

# Column names
locations_table_name = 'locations'
location_name_col = 'location_name'
lat_col = 'lat'
lng_col = 'lng'
state_col = 'state'
country_col = 'country'


class CommonColumns(Base):
    __abstract__ = True


class Locations(CommonColumns):
    __tablename__ = locations_table_name
    location_id = Column(Integer, primary_key=True, autoincrement=True)
    location_name = Column(String())
    lat = Column(Float())
    lng = Column(Float())
