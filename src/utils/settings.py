# PostgreSQL attributes
POSTGRESQL_HOST = 'localhost'
POSTGRESQL_PORT = 5432
POSTGRESQL_DBNAME = 'climbing'
POSTGRESQL_URI = 'postgresql://{host}:{port}/{dbname}'.format(host=POSTGRESQL_HOST,
                                                              port=POSTGRESQL_PORT,
                                                              dbname=POSTGRESQL_DBNAME)

# locations table
locations_table_name = 'locations'
location_name_col = 'location_name'
lat_col = 'lat'
lng_col = 'lng'
