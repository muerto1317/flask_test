from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = ["установка", "первое приложение", "обратная связь"]


@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='ABOUT', menu=menu)


@app.route('/profile/<username>')
def profile(username):
    # print(url_for('profile'))
    # return render_template('index.html', menu=menu)
    return f"Пользователь: {username}"


@app.route('/profile2/<path:username>') # благодаря path всё, что после username добавляется в эту переменную
def profile2(username):
    return f"Пользователь: {username}"


@app.route('/profile3/<int:username>') # можно писать только цифры
def profile3(username):
    return f"Пользователь: {username}"

@app.route('/profile4/<int:username>/<path>') # пишем что угодно после username/. это значит динамически обрабатывать пути
def profile4(username, path):
    return f"Пользователь: {username}, {path}"

if __name__ == '__main__':
     app.run(debug=True)

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('about'))
#     print(url_for('profile', username="myname"))
#     print(url_for('profile2', username="myname"))
#     print(url_for('profile3', username="6789"))
#     print(url_for('profile4', username="6789", path='anythings'))