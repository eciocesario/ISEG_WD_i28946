from flask import Flask
app=Flask(__name__)
@app.route('/')

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/users/<username>')
def show_user(username):
    return f'User: {username}'

from flask import request
@app.route('/login', methods=['GET', 'POST'])
def login ():
    if request.method=='POST':
    #handle loginn logic
        return 'ok'
    
    else:
    #show login form
        @app.route('/login', methods=['POST'])
        def login():
            username=request.form['username']
            password=request.form['password']
            #handle login logic
from flask import make_response
@app.route('/')
def index():
    response=make_response('Hello World!')
    response.headers['Content-Type']

@app.route('/')
def index():
    name='John'
    return render\_template('index.html')