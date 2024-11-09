from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)  

app.config["MONGO_URI"] = "mongodb+srv://venkatasugunadithya:Adithya%400303@cluster0.zvndb.mongodb.net/sign_in?retryWrites=true&w=majority&appName=Cluster0"
mongo = PyMongo(app)
db = mongo.db

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"message": "All fields are required"}), 400

    hashed_password = generate_password_hash(password)
    db.security.insert_one({
        "username": username,
        "email": email,
        "password": hashed_password
    })

    return jsonify({"message": "User registered successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
