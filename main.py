#!/usr/bin/env python

import argparse
import os
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient, DESCENDING
from dotenv import load_dotenv

def create_app():
    # load configuration
    load_dotenv()
    user = os.environ.get("DB_USER")
    pwd = os.environ.get("DB_PASS")
    db_name = os.environ.get("DB_DATABASE")

    # get connection to database
    mongo_uri = f"mongodb://{user}:{pwd}@localhost:27017/{db_name}?authSource=admin"
    client = MongoClient(mongo_uri)
    db = client[db_name]

    # create flask app
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:8001", "https://mattfeng.tech"])

    @app.route("/")
    def home():
        return "api"

    @app.route("/impact")
    def impact_factors():
        impact = db.impact.find_one({}, sort=[("_id", DESCENDING)], projection={"_id": 0})
        return jsonify(impact)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=4000)
