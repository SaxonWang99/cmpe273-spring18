from flask import Flask, jsonify, abort
from flask import request
app = Flask(__name__)

users=[]

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/users', methods=['POST'])
def addUser():
    name = request.form['name']
    user = {'id': len(users)+1, 'name': name}
    users.append(user)
    return jsonify(user)

@app.route('/users/<int:userId>', methods=['GET'])
def getUser(userId):
    if len(users) == 0 or userId > len(users):
        abort(404)
    user = users[0]
    return jsonify(user)

@app.route('/users/<int:userId>', methods=['DELETE'])
def deleteUser(userId):
    if len(users) == 0 or userId > len(users):
        abort(404)
    user = users[userId-1]
    users.remove(user)
    return jsonify({'result': True})