from flask import Flask, render_template

App = Flask(__name__)

@App.route('/')
def index():
    return render_template('index.html')

@App.route('/produto')
def produto():
    return render_template('produto.html')