import csv
from pymongo import MongoClient



list = []
count = 0
client = MongoClient('localhost', 27017)
db = client.testdb
collection = db.tests


with open('C:/Users/kim/Desktop/test.csv', 'r') as csvfile:
    for line in csvfile:
        count += 1
        sp = line.split(',')
        collection.insert_one({"id": sp[0], "category name" : sp[1], "Time" : sp[2] , "gender" : sp[3]})
