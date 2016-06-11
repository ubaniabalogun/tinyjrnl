from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api
from flask.ext.httpauth import HTTPBasicAuth

# Database instance
db = SQLAlchemy()

# Api instance
api = Api(prefix='/v1')
basic_auth = HTTPBasicAuth(realm='tinyjrnl api')
