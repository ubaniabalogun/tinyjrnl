import argparse
from factory import create_app, register_blueprints


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Launch the application')
    parser.add_argument('--config',dest='config',default='dev',help='App configiguration')
    args = parser.parse_args()
    conf = args.config
    config = None
    if conf == 'dev':
        config = 'config.DevConfig'
    elif conf == 'prod':
        config = 'config.ProdConfig'

    app = create_app('app',config)
    with app.app_context():
        from app.resources.jrnls import jrnls
        register_blueprints(app,jrnls)
    app.run()
