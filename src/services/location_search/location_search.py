import psycopg2
import pandas as pd

from src.utils import settings as s


class LocationSearch:

    def __init__(self):
        self.db = psycopg2.connect(dbname=s.POSTGRESQL_DBNAME)

    def query_location_by_name(self, location_name):
        """
        Query locations table by location name for coordinates
        :param location_name: {str}
        :return: {dict}
        """
        query = 'SELECT {lat_col}, {lng_col} ' \
                'FROM {locations_table_name} ' \
                'WHERE {location_name_col} = \'{location_name}\''.format(lat_col=s.lat_col,
                                                                         lng_col=s.lng_col,
                                                                         locations_table_name=s.locations_table_name,
                                                                         location_name_col=s.location_name_col,
                                                                         location_name=location_name)
        locations_df = pd.read_sql(query, con=self.db)
        return {
            'lat': locations_df.ix[0].lat,
            'lng': locations_df.ix[0].lng
        }