#!/home/runner/workspace/.pythonlibs/bin/python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
  return "<button>Hello, World!</button>"


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
