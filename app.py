import os
from eve import Eve
from flask import jsonify
from flask_cors import CORS
from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL

from src.data_store.schemas import Base
from src.services.api_endpoints.locations import Locations

# settings
cur_dir = os.path.dirname(os.path.realpath(__file__))
settings_file = os.path.join(cur_dir, "src/utils/settings.py")

# application
app = Eve(settings=settings_file,
          validator=ValidatorSQL,
          data=SQL)
CORS(app)

db = app.data.driver
Base.metadata.bind = db.engine
db.Model = Base

# register hooks
locations = Locations(app)
app.on_fetched_resource_locations += locations.get_all_locations
app.on_fetched_item_locations += locations.get_locations


@app.route('/')
def index():

    ls = Locations()
    data = ls.query_location_by_name(location_name='Boston')
    return jsonify(data)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=True)
