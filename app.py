from flask import Flask, jsonify
from flask_cors import CORS

from src.services.location_search.location_search import LocationSearch

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():

    ls = LocationSearch()
    data = ls.query_location_by_name(location_name='Boston')
    return jsonify(data)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=True)
