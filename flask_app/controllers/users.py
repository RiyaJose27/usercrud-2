from flask_app import app
from flask import render_template, redirect, session,request
from flask_app.models.user import User





@app.route('/')
def index():
    users = User.get_all_users()
    return render_template("create.html", users=users)


@app.route('/next/add')
def direct():
    return render_template("read.html")


@app.route('/add', methods=['POST'])
def next_form():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    # print(request.form)
    User.insert_all_users(data)
    return redirect('/')


@app.route('/add/next')
def bac():
    return redirect('/')

@app.route('/next/<int:id>/on')
def new(id):
    data = {
    "id" : id
    }
    user = User.get_single_user(data)
    print (user)
    return render_template("one.html", user=user)


@app.route('/on/<int:id>/tw')
def now(id):
    data = {
    "id" : id
    }
    user = User.get_single_user(data)
    print (user)
    return render_template("two.html", user=user)



@app.route('/tw/on')
def second():
    return render_template("one.html")

@app.route('/next/<int:id>/tw')
def first(id):
    data = {
    "id" : id
    }
    user = User.get_single_user(data)
    print (user)
    return render_template("two.html", user=user)


@app.route('/add/next')
def all():
    return redirect('/')