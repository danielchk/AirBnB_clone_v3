#!/usr/bin/python3
"""Status file"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    """Status route to message OK"""
    d = {"status": "OK"}
    return jsonify(d)


@app_views.route('/stats')
def stats():
    """count the different stats"""
    c = {"amenities": storage.count("Amenity"),
         "cities": storage.count("City"),
         "places": storage.count("Place"),
         "reviews": storage.count("Review"),
         "states": storage.count("State"),
         "users": storage.count("User")}
    return jsonify(c)
