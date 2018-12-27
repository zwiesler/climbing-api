from src.data_store.schemas import Locations
from eve_sqlalchemy.config import DomainConfig, ResourceConfig


DOMAIN = DomainConfig({
    'locations': ResourceConfig(Locations)
}).render()

DOMAIN['locations'].update({
    'item_methods': ['GET', 'PATCH', 'PUT'],
    'resource_methods': ['GET', 'POST']
})

X_DOMAINS = '*'
X_HEADERS = ['If-Match', 'Content-Type', 'Authorization']
X_ALLOW_CREDENTIALS = True
BANDWIDTH_SAVER = False
CACHE_CONTROL = 'no-cache'
URL_PREFIX = 'api'
CACHE_EXPIRES = 0
PAGINATION_LIMIT = 10000

# Database configs
POSTGRESQL_HOST = 'localhost'
POSTGRESQL_PORT = 5432
POSTGRESQL_DBNAME = 'climbing'
SQLALCHEMY_DATABASE_URI = 'postgresql://{host}:{port}/{dbname}'.format(host=POSTGRESQL_HOST,
                                                                       port=POSTGRESQL_PORT,
                                                                       dbname=POSTGRESQL_DBNAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False
