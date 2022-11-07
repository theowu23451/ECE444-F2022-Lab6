from flask import Flask


# create a new Flask App
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()