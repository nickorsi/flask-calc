# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.get("/add")
def add():
    a_value = int(request.args.get("a"))
    b_value = int(request.args.get("b"))

    return str(operations.add(a_value, b_value))

@app.get("/sub")
def sub():
    a_value = int(request.args.get("a"))
    b_value = int(request.args.get("b"))

    return str(operations.sub(a_value, b_value))

@app.get("/mult")
def mult():
    a_value = int(request.args.get("a"))
    b_value = int(request.args.get("b"))

    return str(operations.mult(a_value, b_value))

@app.get("/div")
def div():
    a_value = int(request.args.get("a"))
    b_value = int(request.args.get("b"))

    return str(operations.div(a_value, b_value))
