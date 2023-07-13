from flask import Flask
from app import controllers
from app import models

app = Flask(__name__)

app.config.from_object('config')
controllers.init_app(app)