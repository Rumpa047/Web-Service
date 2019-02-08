
from flask import Flask
from pymongo import MongoClient

con = MongoClient()
db = con.mypropertydb
data_table = db.properties


# class data_connection():
#     def success(self):

#         print("MongoDB connectiob done !!")
