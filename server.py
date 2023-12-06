from flask import Flask
from dotenv import load_dotenv
load_dotenv()
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

port = os.getenv("PORT")


@app.route("/api")
def home():
    names = ["Kia", "Kai", "Koa", "Kei", "Kui"]
    ages = [12, 10, 15, 9, 5]
    heights = (1.5, 1.2, 1.7, 1, 0.7)
    return {
        "names": names,
        "ages": ages,
        "heights": heights
    }, 200

@app.route("/api/about")
def about():
    str = "A simple Flask App"
    return str, 200


if __name__=="__main__":
    app.run(port=port, debug=True)