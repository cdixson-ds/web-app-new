# imports
from flask import render_template, make_response, request
from flask import current_app as app
from .models import db, User

@app.route('/', methods = ['GET', 'POST'])
def home():
    print("YAY It worked!")
    return render_template('index.html')

@app.route('/create_user', methods = ['GET', 'POST'])
def create_user():

    if request.method == 'POST':
        name = request.form['username']
        city = request.form['city']
        occupation = request.form['occupation']

        user_exists = User.query.filter(User.name == name).first()
        if user_exists:
            return make_response(f"User {name} already exists!")

        new_user = User(name=name, city=city, occupation=occupation)
        db.session.add(new_user)
        db.session.commit()
        return make_response(f"User {name} Successfully Created!")

@app.route('/display_users', methods = ['GET'])
def display_users():

    users = User.query.all()
    return render_template("our_users.html", users=users)
