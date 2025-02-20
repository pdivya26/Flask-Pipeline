from flask import Flask, jsonify


app = Flask(__name__)


def home():
    return jsonify({"message": "Hello, World!"})


@app.route('/')
def index():
    return home()
