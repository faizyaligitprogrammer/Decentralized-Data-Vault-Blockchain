import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGODB_SETTINGS = {
        'db':os.environ.get('MONGODB_DB_NAME'),
        'username':os.environ.get('MONGODB_USERNAME'),
        'password':os.environ.get('MONGODB_PASSWORD'),
        'authentication_source':os.environ.get('MONGODB_ADMIN_DB'),
        'host':'localhost',
        'port':27017
    }