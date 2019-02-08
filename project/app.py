from flask import Blueprint
from flask_restful import Api
# from resources.all_properties import Properties, Page
from resources.all_properties import Page

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# route
# api.add_resource(Properties, '/properties')
# api.add_resource(Page, '/properties/page=<page_number>')
api.add_resource(Page, '/properties')