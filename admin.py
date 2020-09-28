from flask import Flask , request , jsonify
from flask_cors import CORS 
from flask_pymongo import PyMongo 
from bson import ObjectId
import json
app = Flask(__name__)
# connect your mongodb after installation
app.config["MONGO_URI"]="mongodb+srv://test:test@cluster0.80jod.mongodb.net/collect?retryWrites=true&w=majority"
mongo = PyMongo(app)

CORS(app)
db = mongo.db.demo2

@app.route('/',methods=["GET","POST"])
def getpost():
    if request.method == "GET":
        o =[]
        for i in db.find():
            o.append({"_ID":str(ObjectId(i["_id"])),"name":i["name"],"email":i["email"],"password":i["password"]})
        return jsonify(o)
    elif request.method == "POST":
        id = db.insert({"name":request.json["name"],"email":request.json["email"],"password":request.json["password"]})
        return jsonify(str(ObjectId(id)))
@app.route('/<id>',methods=["DELETE","PUT"])
def deleteput(id):
    if request.method == "DELETE":
        db.delete_one({"_id":ObjectId(id)})
        return jsonify({"message":"deleted"})
    elif request.method == "PUT":
        db.update({"_id":ObjectId(id)},{"$set":{
            "name":request.json["name"],
            "email":request.json["email"],
            "password":request.json["password"]
        }})
        return jsonify({"message":"updated"})
@app.route('/getone/<id>',methods=["GET"])
def getone(id):
    res = db.find_one({"_id":ObjectId(id)})
    print(res)
    return {"_ID":str(ObjectId(res["_id"])),"name":res["name"],"email":res["email"],"password":res["password"]}
