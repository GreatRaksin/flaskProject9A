from flask import Flask

app = Flask(__name__)


@app.route('/')
def main_page():
    return '<h1>Welcome to my site!</h1>'


@app.route('/about')
def about_page():
    return '<h1>About us</h1>'


if __name__ == '__main__':
    app.run(debug=True)
