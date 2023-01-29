from flask import Flask
app=Flask(__name__)
"app.route('/')
def index():
    return 'Hello World!'
@app.route('/users/<username>')
def show_user(username):
    return f'User: {username}'
@app.route('/login', methods=['GET', 'POST'])
df login ():
if request.method=='POST':
#handle loginn logic
else:
#show login form