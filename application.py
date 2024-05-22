from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello There my good man!"


if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=5000)