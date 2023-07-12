from flask import Flask
from app.controllers import default

app = Flask(__name__)

default.init_app(app)