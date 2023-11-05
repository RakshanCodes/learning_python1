# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

# @app.route("/greet")
# def greet():
#     return "Greetings!"


@app.route("/greet")
@app.route("/greet/<name>")
def greet_dhilipsiva(name=None):
    if name is None:
        return "Greetings!"
    else:
        return f"Greetings, {name}!"


"""
ASSIGNMENT: Calculator

/sum/num1/num2  => num1 + num2 = answer
likewise, sub, mul, div
"""
