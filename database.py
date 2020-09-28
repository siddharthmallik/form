import pymongo import MongoClient
import datetime
import sys

from bson.objectid import ObjectId

global con
global db
global recipcol

def connect_db():
    global con
    global db
    global recipcol
    con = MongoClient("mongodb+srv://test:test@cluster0.80jod.mongodb.net/collect?retryWrites=true&w=majority")
    db = con.collect
    recipcol = db.superuser
    return

def save_recipe(savRcpCol):
    global recipcol
    connect_db()
    recipcol.insert(savRcpCol)
    return

def read():
    global recipcol
    connect_db()
    allREcipes = recipcol.find({})
    print(allREcipes)
    return allREcipes

"""
mydb = myclient["collect"]

mycol = mydb["superuser"]
mycol = mydb["gen_user"]

mylist = [
  { "_id": 1, "name": "John", "password": "Highway37"},
  { "_id": 2, "name": "Peter", "password": "Lowstreet27"},
  { "_id": 3, "name": "Amy", "password": "Applest652"},
  { "_id": 4, "name": "Hannah", "password": "Mountain21"},
  { "_id": 5, "name": "Michael", "password": "Valley345"},
  { "_id": 6, "name": "Sandy", "password": "Oceanblvd2"},
  { "_id": 7, "name": "Betty", "password": "GreenGrass1"},
  { "_id": 8, "name": "Richard", "password": "Skyst331"},
  { "_id": 9, "name": "Susan", "password": "Oneway98"},
  { "_id": 10, "name": "Vicky", "password": "YellowGarden2"},
  { "_id": 11, "name": "Ben", "password": "ParkLane38"},
  { "_id": 12, "name": "William", "password": "Centralst954"},
  { "_id": 13, "name": "Chuck", "password": "MainRoad989"},
  { "_id": 14, "name": "Viola", "password": "Sideway1633"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)
"""