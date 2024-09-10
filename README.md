# falsk-mongo

from flask import Flask, request
import pymongo
from pymongo import MongoClient
from flask import jsonify
app = Flask(__name__)
from flask_cors import CORS
cors = CORS(app, resources={r"/*": {"origins": "*"}})
