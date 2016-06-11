from flask.ext.restful import Resource
from app.services.authentication import *


class BaseResource(Resource):
    """
    Base class For Resources
    """
    method_decorators = [] 
    resource_fields = None # Implement this in subclasses

class BasicAuthResource(BaseResource):
    """
    An API Resource that is protected by HTTP BasicAuth
    """
    resource_fields = None
    method_decorators = [basic_auth.login_required]
