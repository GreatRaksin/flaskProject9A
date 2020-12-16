from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/about')
def about_page():
    return '<h1>About us</h1>'


if __name__ == '__main__':
    app.run(debug=True)
