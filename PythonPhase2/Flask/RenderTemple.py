from flask import  Flask,render_template
app = Flask(__name__)
@app.route('/text')
def showtext():
    return render_template('showText.html')
@app.route('/image')
def showimage():
    return render_template('showImage.html')
