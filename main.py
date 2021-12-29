from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:8001", "https://mattfeng.tech"])

@app.route("/")
def home():
    return "api"

@app.route("/impact")
def impact_factors():
    return "0"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
