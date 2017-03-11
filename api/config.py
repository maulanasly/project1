

class BaseConfig():
    pass


class DevelopmentConfig():
    pass


class TestingConfig():
    pass


class StagingConfig():
    pass


class ProductionConfig():
    pass

config = {
    'development': 'api.config.DevelopmentConfig',
    'testing': 'api.config.TestingConfig',
    'staging': 'api.config.StagingConfig',
    'production': 'api.config.ProductionConfig'
}