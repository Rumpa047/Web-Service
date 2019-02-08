import requests
from flask import Flask
from pymongo import MongoClient
import pytest
import run
from resources.all_properties import Page





def test_status_code():
    req = requests.get('http://127.0.0.1:5000/api/properties')
    assert req.status_code == 200

# def test_empty_db():
#     """Start with a blank database."""
#     rv = requests.get('http://127.0.0.1:5000/api/properties')
#     assert b'result' in rv.data

#
# def test_collection_fields():
#     conn = MongoClient()
#     db = conn.mypropertydb
#     data_table = db.properties
#     obj = data_table.findOne()
#     item = 0
#     for i in obj:
#         item+=1
#     assert item == 3
#
# def test_collection_items():
#     conn = MongoClient()
#     db = conn.mypropertydb
#     data_table = db.properties
#     # items = db.properties.count()
#     items = data_table.find().count()
#     assert items == 146
#
# def test_db_port():
#     conn = MongoClient()
#     db = conn.mypropertydb
#     # data_table = db.properties
#     # items = db.properties.count()
#     # items = data_table.find().count()
#     assert db.port == 27017
#  var message = db.messages.findOne();
# > for (var key in message) {
# ... print(key);
#
# def test_page_items():
#     count = 1
#     for i in Page.get(self, 48):
#         count+=1
#     assert count == 48

# def test_main_page():
#     # response = app.api.add_resource('/properties', follow_redirects=True)
#     assert run() ==  True

# def test_page_id():
#     a = type(Page.get().output)

# def test_data_table_name():
#     name = MongoClient().mypropertydb.properties
#
#     manuel = mongodb.players.find_one({'name': 'Manuel'})
#     assert manuel['surname'] == 'Neuer'

# def f():
#     return 3
#
# def test_function():
#     assert f() == 3
