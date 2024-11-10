from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS  # Import CORS
from bson.json_util import dumps

app = Flask(__name__)

# Enable CORS for the specific frontend domain(s)
CORS(app)  # Change to your frontend URL

# MongoDB URI for the 'Challengers' database and 'Challenger' collection
client = MongoClient('mongodb+srv://venkatasugunadithya:Adithya%400303@cluster0.zvndb.mongodb.net/')
db = client.Challengers  # Change the database name to 'Challengers'
challenger_collection = db.Challenger  # Change the collection name to 'Challenger'

@app.route('/add_challenge', methods=['POST'])
def add_challenge():
    data = request.get_json()  # Get JSON data from request
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Insert the challenge data into the 'Challenger' collection in the 'Challengers' database
    result = challenger_collection.insert_one({
        "challenge_name": data.get('challengeName'),
        "challenge_description": data.get('description'),
        "status": data.get('status')
    })
    
    if result.inserted_id:
        return jsonify({"success": True, "message": "Challenge added successfully!"}), 201
    else:
        return jsonify({"error": "Failed to add challenge"}), 500

@app.route('/modify_challenge', methods=['PUT'])
def modify_challenge():
    data = request.get_json()  # Get JSON data from request
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Modify the challenge data in the 'Challenger' collection in the 'Challengers' database
    result = challenger_collection.update_one(
        {"challenge_name": data.get('challengeName')},  # Find challenge by name
        {"$set": {
            "challenge_description": data.get('description'),
            "status": data.get('status')
        }}
    )
    
    if result.modified_count > 0:
        return jsonify({"success": True, "message": "Challenge modified successfully!"}), 200
    else:
        return jsonify({"error": "Challenge not found or no changes made"}), 404

@app.route('/events', methods=['GET'])
def events():
    events = challenger_collection.find()  # Fetch all challenges from the database
    events_list = [event for event in events]  # Convert the cursor to a list
    return dumps(events_list)  # Convert to JSON format and return the response

if __name__ == '__main__':
    app.run(debug=True)
