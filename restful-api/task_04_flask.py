#!/usr/bin/python3

import json, requests
from flask import Flask, jsonify


app = Flask(__name__)

dic_users = {}

#HOME
@app.route('/')
def home():
    return "Welcome to the Flask API!"

#LISTA DE USUARIOS
@app.route('/data', methods=['GET'])
def users():
    return jsonify(list(dic_users.keys()))

#ESTADO
@app.route('/status')
def status():
    return ("OK"), 200

#INFORMACION DE CADA USUARIO
@app.route('/users/<string:username>', methods=['GET'])
def get_username(username):
    user = dic_users.get(username)
    if username:
        return jsonify(user)
    else:
        return ({"error": "User not found"})

#AGRREGAR USUARIO
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json(dic_users)

    username = data.get('username')
    name = data.get('name')
    age = data.get('age')
    city = data.get('city')

    if not username:
        return ({"error":"Username is required"}, 400)

    dic_users[username] = {
        'username': username,
        'name': name,
        'age': age,
        'city': city
    }


if __name__ == '__main__':
    app.run(debug=True)
