# challenge4charity
This project consists of a Flask backend API that interacts with MongoDB, as well as static HTML pages (challenges.html) that allow users to interact with the app. This guide will help you set up the local server for the API and access the webpages.

## Prerequisites

- Python 3.6+ installed on your machine.
- MongoDB account with a MongoDB Atlas cluster (or local MongoDB setup).
- Node.js and npm installed for managing any front-end dependencies if needed (though not required for this setup).
- A web browser to view the webpages.

## Setting Up the Local API (Flask Backend)

1. **Clone the repository** (if applicable) or download the project files to your local machine.

2. **Install required Python packages**:
   - Navigate to the project directory and create a virtual environment (optional but recommended):
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On **Windows**:
       ```bash
       venv\Scripts\activate
       ```
     - On **MacOS/Linux**:
       ```bash
       source venv/bin/activate
       ```
   - Install the necessary Python packages by running:
     ```bash
     pip install -r requirements.txt
     ```

     The `requirements.txt` should include the following:
     ```
     Flask==2.x.x
     Flask-Cors==3.x.x
     pymongo==4.x.x
     bson==4.x.x
     ```

3. **Set up MongoDB connection**:
   - Ensure you have your MongoDB URI and connection credentials. For example:
     ```python
     client = MongoClient('mongodb+srv://username:password@cluster0.mongodb.net/')
     ```

4. **Run the Flask app**:
   - Start the local server by running the following command:
     ```bash
     python app.py
     ```
   - The API server will be running on `http://127.0.0.1:5000`.

5. **Verify the API**:
   - The server should now be running. You can check by navigating to:
     - `http://127.0.0.1:5000/add_challenge` (POST endpoint for adding challenges).
     - `http://127.0.0.1:5000/modify_challenge` (PUT endpoint for modifying challenges).
     - `http://127.0.0.1:5000/events` (GET endpoint for fetching events).

## Accessing the Webpages

1. **Open challenges.html**:
   - Open the `challenges.html` file in your web browser directly.
   - The HTML file will interact with the API running on `http://127.0.0.1:5000`.

2. **Test the webpages**:
   - On the webpage, you should be able to:
     - Add challenges using the modal form.
     - Modify challenges using the modification modal.
     - View events data through the events button (fetched from the backend).
   
3. **Navigate between pages**:
   - Use the "Back to Home" button to navigate back to the main page (assuming you have a `sponsors.html` page available).
   - Make sure that the `sponsors.html` page has the correct routing to handle any requests or changes.

## Troubleshooting

1. **CORS Issues**:
   - If you encounter CORS issues (e.g., `Access to fetch at 'http://127.0.0.1:5000/add_challenge' has been blocked by CORS policy`), ensure that CORS is enabled properly in your Flask app by adding the following:
     ```python
     from flask_cors import CORS
     CORS(app)  # This will allow all origins. For more control, specify origins.
     ```

2. **MongoDB Connection Issues**:
   - Double-check your MongoDB URI, username, password, and cluster name. Ensure your MongoDB Atlas cluster is accessible from your local machine.
   - Ensure that the `Events` collection exists in the MongoDB database specified.

3. **Network Issues**:
   - Ensure that the Flask API is running on `http://127.0.0.1:5000`. If using a different port, update the URL in your HTML/JavaScript accordingly.

4. **API Response Issues**:
   - Check the browser console (Developer Tools > Console) for any errors when interacting with the API, especially if the fetch requests are failing.

---

## Conclusion

You should now have a fully working local environment where you can interact with the Flask API and view the webpages. Make sure your Flask backend and MongoDB are running smoothly, and you should be able to add, modify, and fetch data via the frontend.
