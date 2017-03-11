from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
from flask_restful import Api
from blogsapi.config import config
from blogsapi.exceptions import ApiException

import os

app = Flask(__name__, instance_relative_config=True)

environment = os.getenv('APP_CONFIGURATION', 'testing')
config_file = environment + '.cfg'
app.config.from_object(config[environment])
app.config.from_pyfile(config_file, silent=True)

db = SQLAlchemy(app)

api = Api(app)

from blogsapi.resources.blog import BlogList, BlogDetail

api.add_resource(BlogList, '/blog')
api.add_resource(BlogDetail, '/blog/<string:blog_title>')


@app.errorhandler(ApiException)
def handle_coaching_exception(error):
    data = {
        "reason": error.description,
        "code": error.code
    }
    response = jsonify(data)
    response.status_code = error.status_code
    return response