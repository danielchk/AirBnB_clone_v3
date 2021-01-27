#!/usr/bin/python3
"""endpoint"""
import models
from flask import Flask
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(self):
    """teardown to app"""
    models.storage.close()

if __name__ == "__main__":
    host = getenv("HBNB_API_HOST") or '0.0.0.0'
    port = getenv("HBNB_API_PORT") or 5000
    app.run(host=host, port=port, threaded=True)