from flask import Flask, render_template, request, redirect

app = Flask(__name__)
@app.route('/login2', methods=['GET', 'POST'])
def login2():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == '1234':
            return redirect('http://www.yahoo.co.jp')
        else:
            text="login fail"
            return  render_template('T9And2.html',message=text)
    return render_template('T9And2.html')


