from flask import Flask,url_for,request
app = Flask(__name__)
print(app)
@app.route('/')
def index():
    pass
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
     pass
    else:
     pass
@app.route('/user/<userName>')
def profile(userName):
    pass
with app.test_request_context('/'):
    print(url_for('index',))
    print(url_for('login'))
    print(url_for('login',id=2,usj='233',))
    print(url_for('profile',userName='234'))
    url_for('static',filename='style.css')
