# Simple web application using Flask framework
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Fattie!</p>"

if __name__ == '__main__':
    app.run(host="47.129.158.136", port=80)