from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/user<UserName>')
def user(UserName):
    return render_template('test1.html', name=UserName)
