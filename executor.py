from flask import Flask
from flask import request
import ast

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/execute", methods=['POST'])
def execute():
    json = request.json
    program = json["program"]
    try:
        result = eval(program)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}


@app.route("/validate", methods=['POST'])
def validate():
    json = request.json
    program = json["program"]
    try:
        ast.parse(program)
        return {}
    except SyntaxError as e:
        return {"error": str(e)}
