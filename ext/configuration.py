import os


def init_app(app):
    config = get_config_from_env()
    app.config.from_object(config)


def get_config_from_env():
    envname = os.getenv("FLASK_ENV", "development").lower()
    if envname == "production":
        return ProductionConfig()
    return DevelopmentConfig()


class ProductionConfig:  # pylint: disable=R0903
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False

    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "Ch@nG3_th1s_IN_PR0D!")

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(ProductionConfig):  # pylint: disable=R0903
    FLASK_ENV = "development"
    DEBUG = True
