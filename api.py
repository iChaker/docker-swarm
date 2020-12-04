from flask import Flask
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
import pymongo 

app = Flask(__name__)
client = pymongo.MongoClient(host = "mongodb://mongo", port = 27017, serverSelectionTimeoutMS = 1000)
print(client)
mongo = client.tododb

@app.route('/users')
def todos():
     todos = mongo.db.user.find()
     resp = dumps(todos)
     return resp

@app.route('/adduser', methods = ['POST'])
def add_todo():
    _json = request.json
    _todo = _json['user']

    if _todo and request.method == 'POST':
        id = mongo.db.todo.insert_one({'user': _todo})
        response = jsonify("user  added successfully!")
        response.status_code = 200
        return response
    else:
        return not_found()

@app.errorhandler(404)
def not_found(error = None ):
    message = {
        'status': 404,
        'message': 'Not Found' + request.url
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug = True, use_reloader = True)
