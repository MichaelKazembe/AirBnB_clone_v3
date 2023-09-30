#!/usr/bin/python3
"""
    Retrieves JSON responses
"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def get_status():
    """ Returns JSON status response """
    return jsonify({"status": "OK"})
