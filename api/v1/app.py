#!/usr/bin/python3
"""endpoint for api"""
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)