from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost/pythonreactdb'

mongo = PyMongo(app)

db = mongo.db.users


@app.route('/users', methods=['POST'])
def createUsers():
    return "received"


if __name__ == '__main__':
    app.run(debug=True)
