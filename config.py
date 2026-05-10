
class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root2@localhost:3306/mechanic_db'
    DEBUG = True

class TestConfig:
    pass

class ProductConfig:
    pass


