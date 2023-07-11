from flask import Flask

App = Flask(__name__)

@App.route('/')
def index():
    return 'Olá mundo'