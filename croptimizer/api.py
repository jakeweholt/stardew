from flask import Flask, request, jsonify
import json
app = Flask(__name__)

with open('./mock/mockOutput.json') as file:
  mockOutput = json.load(file);

@app.route('/', methods=['POST'])
def post():
    if request.method == 'POST':
        return mockOutput

@app.route('/', methods=['GET'])
def get():
    if request.method == 'GET':
        testResponse = "curl --url http://127.0.0.1:5000/ -X POST -H \"Content-Type: application/json\" --data '{\"foo\":\"bar\"}'"
        return testResponse