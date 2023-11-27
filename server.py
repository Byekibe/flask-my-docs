from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    names = ["Kia", "Kai", "Koa", "Kei", "Kui"]
    ages = [12, 10, 15, 9, 5]
    height = (1.5, 1.2, 1.7, 1, 0.7)
    return {
        "names": names,
        "ages": ages,
        "height": height
    }, 200

@app.route("/about")
def about():
    str = "A simple Flask App"
    return str, 200


if __name__=="__main__":
    app.run(port=5007, debug=True)