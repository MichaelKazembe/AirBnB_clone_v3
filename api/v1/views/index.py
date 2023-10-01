#!/usr/bin/python3
"""
    Retrieves JSON responses
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """ Returns JSON status response """
    response = jsonify({"status": "OK"})
    response.headers['Content-Type'] = 'application/json'
    return response


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """ Retrieves the number of each object type """
    count_obj = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }
    for obj in count_obj.keys():
        count_obj[obj] = storage.count(count_obj.get(obj))
    response = jsonify(count_obj)
    response.headers['Content-Type'] = 'application/json'
    return response
