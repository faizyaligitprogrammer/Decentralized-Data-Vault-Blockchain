import os

from flask import Flask
from flask_mongoengine import MongoEngine
from main.config import Config

db = MongoEngine()

class User(db.Document):
    username = db.StringField(unique=True, required=True)
    email = db.EmailField(unique=True)
    age = db.IntField()
    bio = db.StringField(max_length=100)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    # user = User(
    #     username="JohnDoe",
    #     email="abc@gmail.com",
    #     age=22,
    #     bio="hello world"
    # ).save()
    return app