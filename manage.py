from flask.ext.script import Manager
from factory import create_app
from app.models import *


app = create_app('app','config.DevConfig')

# Initialize Manager
manager = Manager(app)


@manager.command
def create_db():
    with app.app_context():
        app.db.create_all()

@manager.command
def drop_db():
    user_input = ''
    while user_input not in ['YES','q']:
        user_input = raw_input("DROP Database Tables? [YES,q]")

    if user_input == 'YES':
        with app.app_context():
            app.db.drop_all()
    else:
        return


if __name__ == '__main__':
    manager.run()
