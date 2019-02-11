from flask_restful import Resource 
from flask import Flask
from pymongo import MongoClient
from flask import request


conn = MongoClient()
db = conn.mypropertydb
data_table = db.properties


class Page(Resource):
    def get(self):

        if 'feed_ratio' in request.args and 'page' in request.args:
            feed = request.args['feed_ratio']
            page = request.args['page']
            feed = eval(feed)
            feed_11  = feed[0]['ratio']
            feed_12  = feed[1]['ratio']
            feed_16  = feed[2]['ratio']

            lst_11 = []
            lst_12 = []
            lst_16 = []

            for item in data_table.find():
                if item['feed'] == "11":
                    lst_11.append({'property_name': item['property_name'], 'Feed': item['feed'], 'Price': item['price']})
                
                elif item['feed'] == "12":
                    lst_12.append({'property_name': item['property_name'], 'Feed': item['feed'], 'Price': item['price']})
                
                else: 
                    lst_16.append({'property_name': item['property_name'], 'Feed': item['feed'], 'Price': item['price']})
            
            output = []
            position_11 = (int(page) - 1) * feed_11
            position_12 = (int(page) - 1) * feed_12
            position_16 = (int(page) - 1) * feed_16

            for i in range(position_11, position_11 + feed_11):
                output.append(lst_11[i])
            
            for i in range(position_12, position_12 + feed_12):
                output.append(lst_12[i])

            for i in range(position_16, position_16 + feed_16):
                output.append(lst_16[i])
            

            
            return output
            # return feed[0]['ratio'], feed[0]['feed']
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


    
