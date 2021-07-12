from flask import Flask

app = Flask(__name__)
# __name__ = main.py


@app.route("/")
def print_hello():
    return "<h1>Hello World!</h1>"


if __name__ == '__main__':
    app.run()
