from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

@app.route('/loop')
def loopy():
    return render_template('index.html')
