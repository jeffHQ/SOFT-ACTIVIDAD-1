from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello():

    return '<h1>Los quiero, World!</h1>'