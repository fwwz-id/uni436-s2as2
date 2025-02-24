import os

from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://127.0.0.1:27017")

client = MongoClient(MONGODB_URI)
db = client["esp32-sensors"]

@app.route("/ping")
def ping():
    return jsonify({"message": "pong"})

@app.route("/dht22", methods=["GET"])
def get_dht22():
    dht22 = db["dht22"]
    data = dht22.find({})
    return jsonify({"data": list(data)})


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)