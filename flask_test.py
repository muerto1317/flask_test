from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Главная страница')


@app.route('/about')
def about():
    return render_template('about.html', title='ABOUT')


if __name__ == '__main__':
    app.run(debug=True)
