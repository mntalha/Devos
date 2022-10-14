
# importing module
from pymongo import MongoClient
 
# creation of MongoClient
client=MongoClient()
 
# Connect with the portnumber and host
client = MongoClient("mongodb://localhost:27017/")
 
# Create database
mydatabase = client["test_database"]
 
# Access collection of the database
mycollection=mydatabase["myTable"]
 
# dictionary to be added in the database
rec={
title: "MongoDB and Python",
description: "MongoDB is no SQL database",
tags: ["mongodb", "database", "NoSQL"],
}
 
# inserting the data in the database
rec = mydatabase.myTable.insert(record)