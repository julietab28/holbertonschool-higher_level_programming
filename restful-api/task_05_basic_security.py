#!/usr/bin/python3

from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
jwt = JWTManager(app)
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

@app.route('/')
def home():
    return "holas"

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    else:
        return None

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
    return "JWT Auth: Access Granted", 200

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    curent_user = get_jwt_identity()
    return "Admin Access Granted", 200

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run()