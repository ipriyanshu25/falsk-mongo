from flask import Flask, request
import pymongo
from pymongo import MongoClient
from flask import jsonify
app = Flask(__name__)
from flask_cors import CORS
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World 1!</p>"
# @app.route("/home")
# def home():
#     return "<p><b>Name</b> PsYadav</p>"
# @app.route("/contact")
# def contact():
#     return "<p><b>Contact</b>12345678</p>"

# @app.route("/ifelse")
# def conditional():
#     value = 1
#     if value == 2:
#         return "<p>Value is 2</p>"
#     elif value<2:
#         return "<p>Value is less than 2</p>"
#     else:
#         return "<p>Value is not 2</p>"
    

# @app.route("/inline")
# def conditional1():
#     value = 1
#     # if value==1:
#     #   msg = "equal"
#     # else:
#     #    msg = "not equal"

#     msg = "value equal to 1" if value == 1 else "value not equal 1"        # another method to write the if else in single line
#     return msg

# @app.route("/for-loop")
# def forloop():
#     marks = [1, 2, 3, 4, 5]
#     totalmark = 0
#     for mark in marks:
#         totalmark += int(mark)
#     return {
#         "status":1,
#         "message":"Sucess",
#         "playload":{"totalmark : ": totalmark , "value":marks}
#     }
    

# @app.route("/while-loop")
# def whileloop():
#     i = 0
#     marks = []
#     while i < 10:
#         i+=1
#         marks.append(i)
#     return{
#          "status":1,
#          "message":"Sucess",
#          "playload":{"marks : ": marks , "value":i}
#      }


# @app.route("/do-while-loop")
# def dowhileloop():
#     i = 9
#     marks = []
#     while True:
#         i+=1
#         marks.append(i)
#         if i>9:
#             break
#     return{
#          "status":1,
#          "message":"Sucess",
#          "playload":{"marks : ": marks , "value":i}
#     }


# def addition(arg1,arg2):
#     print(arg1)
#     print(arg2)
#     return arg1 + arg2


# @app.route("/function")
# def pythonfunction():
#     value = addition(arg2=12,arg1=13)
#     return{
#          "status":1,
#          "message":"Sucess",
#          "playload":{"value :":value}
#     }


# @app.route("/function1/<values>")       dynamic function
# def pythonfunction1(values):
#     # values = [1, 2, 3]
#     return ({
#         "status": 1,
#         "message": "Success",
#         "payload": f"value: the message is{values}"})


# def multiply(arg,arg1):
#     return arg*arg1


# @app.route("/function")
# def pythonfunction():
#     value = addition(arg2=12,arg1=13)
#     return{
#          "status":1,
#          "message":"Sucess",
#          "playload":{"value :":value}
#     }


client = MongoClient("mongodb://localhost:27017/")
db = client["glav1"]
# collection = db['useres']

# @app.route("/db")
# def database():
#     # user = {
#     #     '_id': 1,
#     #     'name': "sara",c
#     #     'email': 'johndoe@example.com'
#     # }
#     users = [
#         {'_id': 2, 'name': "john", 'email': 'john@example.com', },
#         {'_id': 3, 'name': "alice", 'email': 'alice@example.com',},
#         {'_id': 4, 'name': "bob", 'email': 'bob@example.com',},
#     ]
#     filter = {"name": "john"}
#     update = {"$set": {"age": 30}}

    # collection.insert_many(users)
    # collection.update_many(filter,update)
    # collection.update_one({'_id': user['_id']}, {'$set': user}, upsert=True)   #for inserting one data/update databse
    # return "Document inserted or updated successfully!"


# @app.route("/db/read")
# def read():
#     # user = collection.find_one({'_id': 2})
#     # users = collection.find({'age': 30})
#     userone = collection.find_one({'_id': 1},{'_id':0})
#     users = collection.find({'age':30},{'name':0,'_id':0})
#     # return user

#     foundList = []
#     for user in users:
#         foundList.append(user)
#     secondList = []
#     for user in users: 
#         secondList.append(user)
    

#     print("users: ",user)
#     return{'foundList':foundList, "secondlist":secondList,"userone":userone}

# @app.route("/update")
# def update():
    # user = collection.find_one({'_id':2})
    # collection.update_one({"_id":2},{"$set":{"address":{"location":"abcd","state":"UP","pincode":281406}}})
    # collection.update_one({"_id":2},{"$set":{'address.location':'glauniversity'}})
    # collection.update_many({},{"$set":{'address.location':'glauniversity'}})
    # update1 = collection.find_one({'_id':2})
    # return{"user":user,"update":update1}

#     updateList = []
#     for user in collection.find({}):    another method of making list in a line and first method is given above in /db/read section
#         updateList.append(user)

# @app.route("/delete")
# def delete():
#     db.useres.delete_one({'_id': 2})
#     return "Document deleted successfully!"

# @app.route("/db/update2")

# def update1():
#     updatuser1=collection.update_one({'_id':1},{'$set':{'email':"rkx1234567@gmail.com","password":1234567}} )
#     return "Document updated successfully!"

# @app.route("/login", methods=['POST'])
# def login():
#     input_data = request.get_json()
#     email = input_data['email']
#     password = input_data['password']
#     user = db.useres.find_one({'email':email,'password':password})
#     if user and '_id' in user:
#         return{
#             'status':1,
#             'msg':"user exits",
#             'classs':"success"
#         }
#     else:
#         return{
#             'status':0,
#             'msg':"user not exits",
#             'classs':"danger"
#         }
    

@app.route("/register", methods=['POST'])
def register():
    input_data = request.get_json()
    name = input_data.get('username')
    email = input_data.get('email')
    password = input_data.get('password')
    phonenumber = input_data.get('phonenumber')
    user = db.useres.find_one({'email':email})
    print(user)
    if user and '_id' in user:
        return {
            'status': 0,
            'msg':"user exit",
            'class':"success"
        }
    count = db.useres.count_documents({})
    users={
        "_id":count+1,
        "name":name,
        "email":email,
        "password":password,
        "phonenumber":phonenumber
    }
    db.useres.insert_one(users)
    return "inserted successfully"


@app.route("/getdata")
def getdata():
    users = []
    for user in db.useres.find():
        users.append(user)
    return users




# import db from './db';

# const fetchData = async () => {
#   const collection = db.collection('your_collection_name');
#   const data = await collection.find().toArray();
#   return data;
# };


# import React, { useState, useEffect } from 'react';
# import fetchData from './fetchData';

# const DataTable = () => {
#   const [data, setData] = useState([]);

#   useEffect(() => {
#     fetchData().then((data) => setData(data));
#   }, []);

#   return (
#     <table>
#       <thead>
#         <tr>
#           <th>Column 1</th>
#           <th>Column 2</th>
#           <!-- Add more columns as needed -->
#         </tr>
#       </thead>
#       <tbody>
#         {data.map((item) => (
#           <tr key={item._id}>
#             <td>{item.column1}</td>
#             <td>{item.column2}</td>
#             <!-- Add more columns as needed -->
#           </tr>
#         ))}
#       </tbody>
#     </table>
#   );
# };

# export default DataTable;