# coding:utf-8
from flask import Flask
from flask import request, render_template

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template('tpl/home.html')


@app.route('/signin', methods=['GET'])
def sign_form():
    return render_template('tpl/')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    return 'Hello, ', username


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



