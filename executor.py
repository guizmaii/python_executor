from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/execute", methods=['POST'])
def execute():
    json = request.json
    program = json["program"]
    return { "result": eval(program) }