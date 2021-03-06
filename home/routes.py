import os
from flask import request, redirect, url_for, render_template, flash, Response
from home import app
from home.models import User, Image
from home.database import db_session
from flask.ext.login import LoginManager, login_user, login_required, logout_user
from home.camera import Camera
from home.camera import make_image
from home.forms import LoginForm

login_manager = LoginManager()
login_manager.init_app(app)

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

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_page')
def video_page():
    return render_template('video.html')

@app.route('/show', methods=['GET', 'POST'])
@login_required
def show_picture():
    if request.method == 'GET':
        pi = Image.query.all()
        return render_template('show_picture.html', picture=None, pi=sorted(pi, reverse=True))
    elif request.method == 'POST' and 'Delete' in request.form:
        pic = request.form.get('Picture')
        db_session.query(Image).filter_by(image=pic).delete()
        db_session.commit()
        os.remove(os.path.join(app.static_folder, pic))
        pi = Image.query.all()
        return redirect(url_for('show_picture', pi=sorted(pi, reverse=True)))


@app.route('/new', methods=['GET', 'POST'])
@login_required
def create_picture():
    if request.method == 'POST' and request.form:
        pic = make_image()
        db_session.add(Image(pic))
        db_session.commit()
        flash("so, here's your image")
        return render_template('show_picture.html', picture=pic, pi=None)
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
#@login_required
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('index'))

