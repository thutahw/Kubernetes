#!/usr/bin/env python3
import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def get_meme():

    response = requests.get(url="https://meme-api.herokuapp.com/gimme")
    return jsonify(response.json()), 200

if __name__ == "__main__":
    app.run(host= '0.0.0.0')