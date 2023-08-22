from flask import Flask
from markupsafe import escape
from flask import url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def hi(name):
    return f'my name is {escape(name)}'

@app.route('/test')
def test():
    print(url_for('hello'))
    print(url_for('hi',name='123'))
    print(url_for('test'))
    print(url_for('test',baa='foo'))
    return "test page"