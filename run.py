# Load environment variables
from dotenv import load_dotenv
import os
load_dotenv()

from flask import Flask
import json


app = Flask("frontend-flask")
app.config["DEBUG"] = True

# Main page
@app.route("/", methods=["GET"])
def homepage():
    return app.send_static_file("index.html")

# Health Check
@app.route("/health", methods=["GET"])
def health():
    return {"status": "UP"}

# Expose endpoint
@app.route('/getsomething', methods=['GET'])
def get_something():
    message_from_env = os.getenv("PYTHON_CUSTOM_MESSAGE")
    return {"message": message_from_env}

app.run(host='0.0.0.0', port=8080, threaded=True)