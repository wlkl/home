import os
from flask import request, redirect, url_for, render_template, flash
from home import app
from home.models import User
from flask.ext.login import LoginManager, login_user, login_required, logout_user
#from home.camera import make_image
from home.forms import LoginForm

login_manager = LoginManager()
login_manager.init_app(app)
last_picture = ""

@login_manager.user_loader
def load_user(userid):
    user = User.query.filter_by(id=int(userid)).first()
    if user:
        return user
    return None


@app.route('/')
@app.route('/index')
#@login_required
def index():
    return render_template('index.html')

@app.route('/show')
@login_required
def show_picture():
    return render_template('show_picture.html', picture=last_picture)

@app.route('/new', methods=['GET', 'POST'])
@login_required
def create_picture():
    pic = last_picture
    if request.method == 'POST' and request.form:
        pic = make_image()
        flash('so make an image')
        return render_template('show_picture.html', picture=pic)
    elif request.method == 'GET':
        flash('no image yet')
        return render_template('new.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(name=request.form['username']).first()
        if user:
            if user.check_password(request.form['password']):
                login_user(user)
                return redirect(url_for('index'))
            else:
                error = 'bad password, try again'
                return render_template('login.html', error=error)
        else:
            error = 'bad username, try again'
            return render_template('login.html', error=error)
    return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('index'))