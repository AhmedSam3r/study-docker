from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World! updated one'


@app.route('/new/hello')
def new_hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')
