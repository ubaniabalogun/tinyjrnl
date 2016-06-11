from factory import create_app, register_blueprints, initialize_api
app = create_app('app','config.DevConfig')
ctx = app.test_request_context()
ctx.push()
from app.models import *
