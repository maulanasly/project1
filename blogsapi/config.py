class BaseConfig(object):
    pass


class DevelopmentConfig():
    pass


class TestingConfig():
    APP_MODE = "unit_test"
    TESTING = True
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://localhost/open-minded-test"

    SITE_NAME = "opn-minded-blogsapi.test"

    FIXTURES_DIRS = ['../fixtures']


class StagingConfig():
    pass


class ProductionConfig():
    pass

config = {
    'development': 'blogsapi.config.DevelopmentConfig',
    'testing': 'blogsapi.config.TestingConfig',
    'staging': 'blogsapi.config.StagingConfig',
    'production': 'blogsapi.config.ProductionConfig'
}