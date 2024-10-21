#!/usr/bin/python3

from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
jwt_manager = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "abcdefghijklmnopqrstuvwxyz"

users = {
    "user1": {
        "username": "user1", 
        "password": generate_password_hash("password"), 
        "role": "user"
        },
    "admin1": {
        "username": "admin1", 
        "password": generate_password_hash("password"), 
        "role": "admin"
        }
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    else:
        return ("401 Unauthorized"), 401

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def authenticator():
    return ("Basic Auth: Access Granted"), 200

@app.route('/login', methods=['POST'])
def login(username, password):
    user = users.get(username)
    payload = {
            "username": "username",
            "password": "password"
        }
    if user and check_password_hash(user['password'], password):
        token = create_access_token(identity=payload)
        return jsonify(access_token=token), 200
    else:
        return jsonify({"invalid username or password "}), 401

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def auth_token():
    return ("JWT Auth: Access Granted"), 200

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    curent_user = get_jwt_identity()
    return ("Admin Access Granted"), 200

@app.route('/')
def home():
    return "holas"

if __name__ == '__main__':
    app.run()