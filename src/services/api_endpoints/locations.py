import psycopg2
import pandas as pd

from src.utils import settings as s
from src.data_store import schemas as sch
from src.services.api_endpoints import locations_utils as lutils


class Locations(object):

    def __init__(self, app):
        self.app = app
        self.db = psycopg2.connect(dbname=s.POSTGRESQL_DBNAME)

    @staticmethod
    def get_locations(response):
        """Return location locationName"""
        return response['location_name']

    def get_all_locations(self, items):
        """Returns all location locationNames in the system"""
        new_items = []
        for item in items['_items']:
            new_items.append(self.get_locations(response=item))

        items['_items'] = new_items

    def query_location_by_name(self, location_name, cols, query_type='coordinates'):
        """
        Query locations table by location name for coordinates
        :param location_name: {str}
        :param cols: {list of str}
        :param query_type {str}
        :return: {dict}
        """
        return_type_dict = {
            'coordinates': lutils.retrieve_coordinates,
            'tab': lutils.retrieve_tab
        }

        query = 'SELECT {cols} ' \
                'FROM {locations_table_name} ' \
                'WHERE {location_name_col} = \'{location_name}\''.format(cols=', '.join(cols),
                                                                         locations_table_name=sch.locations_table_name,
                                                                         location_name_col=sch.location_name_col,
                                                                         location_name=location_name)
        locations_df = pd.read_sql(query, con=self.db)
        return return_type_dict[query_type](locations_df=locations_df)
