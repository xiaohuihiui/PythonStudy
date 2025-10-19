from flask import Flask
app = Flask(__name__)
print(app)
@app.route('/book/<book_name>')
def book(book_name):
    return "book " + book_name
@app.route('/user/<int:user_id>')
def user(user_id):
    return "user " + str(user_id)


