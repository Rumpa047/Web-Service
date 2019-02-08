from flask_restful import Resource 
from flask import Flask, jsonify,json
from pymongo import MongoClient
from flask import request


conn = MongoClient()
db = conn.mypropertydb
data_table = db.properties

# class Properties(Resource):
#     def get(self):
#         output = []
#         for item in data_table.find():
#             output.append({'property_name' : item['property_name'], 'Feed' : item['feed'], 'Price' : item['price']})
#         return {'result' : output}


class Page(Resource):
    def get(self):
        if 'feed_ratio' in request.args:
            feed = request.args['feed_ratio']
            feed = eval(feed)
            return feed[0]['ratio'], feed[0]['feed']
        # rto = []
        # for i in eval(feed):
        #     if 'ratio' in i:
        #         rto.append(i.ratio)
        # return rto


        elif 'page' not in request.args:
            output = []
            for item in data_table.find():
                output.append({'property_name': item['property_name'], 'Feed': item['feed'], 'Price': item['price']})
            return {'result': output}

        else:
            page_number = request.args['page']
            output = []
            x = (int(page_number) - 1) * 48
            for item in data_table.find().skip(x).limit(48):
                output.append({'property_name': item['property_name'], 'Feed': item['feed'], 'Price': item['price']})
            return {'result': output}


    
