import serverless_wsgi
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Home Section!</p>"

@app.route("/about")
def about():
    return "<p>About Section!</p>"

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)