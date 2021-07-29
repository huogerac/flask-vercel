from ext import configuration, api, database
from models.users import *


def create_app(**config):

    app = api.create_api_app()
    configuration.init_app(app, **config)
    database.init_app(app, **config)
    return app
