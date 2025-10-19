from flask import Flask
from bookAndUser import app
from functiongetUrl import  app
from RenderTemple import  app

@app.route('/')
def hello():
    return "こんにちは、Flaskアプリです！"
@app.route('/test')
def printinfo():
    return "print info "

if __name__ == '__main__':
    app.run(debug=True)