import logging
from flask import Flask, request, jsonify, redirect
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = "mongodb+srv://venkatasugunadithya:Adithya%400303@cluster0.zvndb.mongodb.net/sign_in?retryWrites=true&w=majority&appName=Cluster0"
mongo = PyMongo(app)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    logging.info("Received request on /register endpoint")

    if request.method == 'POST' or request.method == 'GET':
        if request.content_type == 'application/json':
            data = request.get_json()
            logging.debug(f"Received data: {data}")

            username = data.get('username')
            email = data.get('email')
            password = data.get('password')

            if not username or not email or not password:
                logging.warning("Missing fields in registration request")
                return jsonify({"message": "All fields are required"}), 400

            try:
                hashed_password = generate_password_hash(password)
                mongo.db.security.insert_one({
                    "username": username,
                    "email": email,
                    "password": hashed_password
                })
                logging.info("User registered successfully")
                return jsonify({"message": "User registered successfully!"}), 201
            except Exception as e:
                logging.error(f"Error inserting into MongoDB: {e}")
                return jsonify({"message": "Internal Server Error"}), 500
        else:
            logging.warning("Request with incorrect Content-Type received")
            return jsonify({"message": "Content-Type must be application/json"}), 415
    else:
        logging.warning("Method not allowed on /register endpoint")
        return jsonify({"message": "Method not allowed"}), 405

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    logging.info("Received request on /login endpoint")

    if request.content_type == 'application/json':
        data = request.get_json()
        logging.debug(f"Received data: {data}")

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            logging.warning("Missing fields in login request")
            return jsonify({"message": "Both username and password are required"}), 400

        # Check if the user exists in the database
        user = mongo.db.security.find_one({"username": username})

        if user and check_password_hash(user['password'], password):
            # On successful login, redirect to another site or return a success message
            logging.info("User authenticated successfully")
            return jsonify({"message": "Login successful!"}), 200
        else:
            logging.warning("Invalid username or password")
            return jsonify({"message": "Invalid username or password"}), 401
    else:
        logging.warning("Request with incorrect Content-Type received")
        return jsonify({"message": "Content-Type must be application/json"}), 415

if __name__ == '__main__':
    app.run(debug=True)
