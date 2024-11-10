from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS  # Import CORS
from bson.json_util import dumps

app = Flask(__name__)

# Enable CORS for all domains (you can specify specific origins if needed)
CORS(app)

# MongoDB URI
client = MongoClient('mongodb+srv://venkatasugunadithya:Adithya%400303@cluster0.zvndb.mongodb.net/')
db = client.Sponsors
events_collection = db.Events

@app.route('/add_event', methods=['POST'])
def add_event():
    data = request.get_json()  # Get JSON data from request
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Insert the event data into the database
    result = events_collection.insert_one({
        "event_name": data.get('eventName'),
        "event_date": data.get('eventDate'),
        "event_description": data.get('eventDescription'),
        "venue": data.get('venue'),
        "nature": data.get('nature')
    })
    
    if result.inserted_id:
        return jsonify({"success": True, "message": "Event added successfully!"}), 201
    else:
        return jsonify({"error": "Failed to add event"}), 500

@app.route('/modify_event', methods=['PUT'])
def modify_event():
    data = request.get_json()  # Get JSON data from request
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Modify the event data in the database
    result = events_collection.update_one(
        {"event_name": data.get('eventName')},  # Find event by name
        {"$set": {
            "event_date": data.get('eventDate'),
            "event_description": data.get('eventDescription'),
            "venue": data.get('venue'),
            "nature": data.get('nature')
        }}
    )
    
    if result.modified_count > 0:
        return jsonify({"success": True, "message": "Event modified successfully!"}), 200
    else:
        return jsonify({"error": "Event not found or no changes made"}), 404

if __name__ == '__main__':
    app.run(debug=True)
