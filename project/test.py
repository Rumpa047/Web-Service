import requests
from pymongo import MongoClient
import pytest
import run


def test_status_code():
    app = run.create_app()
    clint = app.test_client()
    res = clint.get('api/properties')
    assert res.status_code == 200

def test_page_items():
    app = run.create_app()
    clint = app.test_client()
    res = clint.get('api/properties?page=1')
    data = res.get_json()
    assert len(data['result']) == 48


def test_empty_page():
    app = run.create_app()
    clint = app.test_client()
    res = clint.get('api/properties?page=6')
    data = res.get_json()
    assert len(data['result']) == 0

def test_collection_items():
    conn = MongoClient()
    db = conn.mypropertydb
    data_table = db.properties
    items = 0
    for item in  data_table.find():
        items+=1

    app = run.create_app()
    clint = app.test_client()
    res = clint.get('api/properties')
    data = res.get_json()

    assert items == len(data['result'])





