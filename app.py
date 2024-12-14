from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/data', methods=['GET'])
def get_data():
    """API route to send data to the Next.js frontend"""
    return jsonify({"message": "Hello from Flask nnn!"})

@app.route('/api/login', methods=['POST'])
def login_user_api():
    # Get the email and password from the request
    return jsonify({'success'}), 200