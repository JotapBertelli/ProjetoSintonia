from flask import Flask, render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html')

@app.route('/home')
def home():
    return render_template('Home.html')

if __name__ == '__main__':
    app.run()
