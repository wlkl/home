from flask import request, session, redirect, url_for, abort, render_template, flash
from home import app
from home.models import User
from flask.ext.login import LoginManager, login_user, login_required
from home.forms import LoginForm

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
    user = User.query.filter_by(id=int(userid)).first()
    if user:
        return user
    return None


@app.route('/testbd')
def testbd():
    res = User.query.all()
    return render_template('test.html', res=res)


@app.route('/')
@login_required
def show_picture():
    return render_template('show_picture.html')


@app.route('/new', methods=['POST'])
@login_required
def create_picture():
    if not session.get('logged_in'):
        abort(401)
    return redirect(url_for('show_picture'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = User.query.filter_by(name=request.form['username']).first()
        if user:
            if user.check_password(request.form['password']):
                login_user(user)
                return redirect(url_for('logout'))
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
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_picture'))