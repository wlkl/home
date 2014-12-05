from app import app
from flask import request, session, redirect, url_for, abort, render_template, flash


@app.route('/')
def show_picture():
    return render_template('show_picture.html')

@app.route('/new', methods=['POST'])
def create_picture():
    if not session.get('logged_in'):
        abort(401)
    return redirect(url_for('show_picture'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_picture'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_picture'))