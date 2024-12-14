from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/data', methods=['GET'])
def get_data():
    """API route to send data to the Next.js frontend"""
    return jsonify({"message": "Hello from Flask nnn!"})

@app.route('/api/login', methods=['POST','GET'])
def login_user_api():
    # Get the email and password from the request
    return "at login page"

@app.route('/login', methods=['POST'])
def login():
    # Parse input data from the request
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Print email and password for debugging
    print(f"Email: {email}, Password: {password}")

    # Return email and password as a response
    return jsonify({"email": email, "password": password}), 200