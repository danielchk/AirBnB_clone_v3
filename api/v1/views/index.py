#!/usr/bin/python3
"""Status file"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """Status route to message OK"""
    d = {"status": "OK"}
    return jsonify(d)


@app_views.route('/stats', strict_slashes=False)
def stats():
    """Use the new count in the obj clss"""
    c = {"amenities": storage.count("Amenity"),
         "cities": storage.count("City"),
         "places": storage.count("Place"),
         "reviews": storage.count("Review"),
         "states": storage.count("State"),
         "users": storage.count("User")}
    return jsonify(c)
