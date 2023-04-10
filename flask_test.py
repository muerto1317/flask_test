from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>основная страничка</h1>'


@app.route('/about')
def about():
    return '<h2>о сайте</h2>'


if __name__ == '__main__':
    app.run(debug=True)
