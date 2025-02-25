import os

from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://127.0.0.1:27017")

client = MongoClient(MONGODB_URI)
db = client["esp32-sensors"]


@app.route("/ping")
def ping():
    return jsonify({"message": "pong"})


@app.route("/dht22", methods=["POST"])
def post_dht22():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['temperature', 'humidity', 'timestamp']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
            
        # Insert into MongoDB
        dht22 = db["dht22"]
        result = dht22.insert_one({
            'temperature': data['temperature'],
            'humidity': data['humidity'],
            'timestamp': data['timestamp']
        })
        
        return jsonify({
            'message': 'Data added successfully',
            'id': str(result.inserted_id)
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Add a new route for the HCSR Motion Sensor
@app.route("/hcsr", methods=["POST"])
def post_hcsr():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['motion', 'timestamp']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
            
        # Insert into MongoDB
        hcsr = db["hcsr"]
        result = hcsr.insert_one({
            'motion': data['motion'],
            'timestamp': data['timestamp']
        })
        
        return jsonify({
            'message': 'Data added successfully',
            'id': str(result.inserted_id)
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
