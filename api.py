from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import json

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'rest'
app.config['MONGO_URI'] = 'mongodb://127.0.0.1/rest'

mongo = PyMongo(app)

@app.route('/api/add', methods=['POST'])
def add_user():
    api = mongo.db.user

    uid = request.json['uid']
    name = request.json['name']
    date = request.json['date']
    md5checksum = request.json['md5checksum']

    user_id = api.insert({'uid' : uid, 'name' : name, 'date' : date, 'md5checksum' : md5checksum})
    new_user = api.find_one({'_id': user_id})

    output = {'uid' : new_user['uid'], 'name' : new_user['name'], 'date' : new_user['date'], 'md5checksum' : new_user['md5checksum']}
    
    return jsonify({'result' : output})

@app.route('/api/show', methods=['GET'])
def get_uid_and_date():
    uid = request.args.get('uid')
    date = request.args.get('date')
#    return uid + " " + date

    api = mongo.db.user

    output = []

    for q in api.find({ 'uid' : uid, 'date' : {'$regex' : '.*' + date + '.*'}}):
        output.append({'uid' : q['uid'], 'name' : q['name']}) 

    return jsonify({'result' : output})

@app.route('/api/count', methods=['GET'])
def get_count():
    uid = request.args.get('uid')
    date = request.args.get('date')
#    return uid + " " + date

    api = mongo.db.user

    results = api.find({ 'uid' : uid, 'date' : {'$regex' : '.*' + date + '.*'}})

    output = results.count() 

    return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=int("8080"),
        debug=True
    )

