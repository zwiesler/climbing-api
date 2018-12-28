import os
import json
import logging

from src.data_store.schemas import Locations
from eve_sqlalchemy.config import DomainConfig, ResourceConfig

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s', )


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

POSTGRESQL_HOST = ''
POSTGRESQL_PORT = ''
POSTGRESQL_DBNAME = ''
GOOGLE_CRED = ''
CLIMBING_SHEET_ID = ''

# get SECRETS
file_path = os.getenv("SECRETS_JSON", None)
if file_path is None:
    logging.error("ENVAR SECRETS_JSON not set")

if file_path is not None:
    with open(file_path) as fin:
        vars_ = json.load(fin)
        for name, value in vars_.iteritems():
            globals()[name] = value

# Database configs
SQLALCHEMY_DATABASE_URI = 'postgresql://{host}:{port}/{dbname}'.format(host=POSTGRESQL_HOST,
                                                                       port=POSTGRESQL_PORT,
                                                                       dbname=POSTGRESQL_DBNAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False
