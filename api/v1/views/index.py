#!/usr/bin/python3
"""
    Retrieves JSON responses
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.place import Place


@app_views.route('/status', methods=['GET'])
def status():
    """ Returns JSON status response """
    response = jsonify({"status": "OK"})
    response.headers['Content-Type'] = 'application/json'
    return response


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """ Retrieves the number of each object type """
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    response = jsonify(stats)
    response.headers['Content-Type'] = 'application/json'
    return response
