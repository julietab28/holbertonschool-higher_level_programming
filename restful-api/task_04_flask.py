#!/usr/bin/python3

import json, requests
from flask import Flask, jsonify


app = Flask(__name__)

dic_users = {
        "jane": {
            "username": "jane",
            "name": "Jane",
            "age": 28,
            "city": "Los Angeles"
            }, 
        "john": {
            "username": "john",
            "name": "John",
            "age": 30,
            "city": "New York"
            }
        }

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def users():
    for key in dic_users:
        return list(dic_users.keys())

@app.route('/status')
def status():
    return("OK")

@app.route('/users/<string:username>', methods=['GET'])
def get_username(username):
    user = dic_users.get(username)
    if username:
        return jsonify(user)
    else:
        return {"error": "User not found"}
# @app.route('/add_user', methods=['POST'])
# def add_user():
if __name__ == '__main__':
    app.run(debug=True)
