from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from openpyxl import load_workbook
import os
import uuid

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'default-secret-key')  # Set via env var in production
jwt = JWTManager(app)

# Mock user database (replace with real DB like SQLite or PostgreSQL)
users = {
    'admin': generate_password_hash('password')
}

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username in users and check_password_hash(users[username], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/files', methods=['GET'])
#@jwt_required()
def get_files():
    files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.xlsx')]
    return jsonify(files=files), 200

@app.route('/append', methods=['POST'])
#@jwt_required()
def append_to_excel():
    data = request.get_json()
    filename = data.get('filename')
    qr_data = data.get('qr_data')
    print("filename:", repr(filename))  # Add this
    print("qr_data:", repr(qr_data)) 

    if not filename or not qr_data:
        return jsonify({'error': 'Filename and qr_data required'}), 400
    
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(filepath):
        return jsonify({'error': 'File not found'}), 404
    
    try:
        wb = load_workbook(filepath)
        ws = wb.active
        ws.append([qr_data])  # Append as new row with single cell
        wb.save(filepath)
        return jsonify({'message': 'Data appended successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)