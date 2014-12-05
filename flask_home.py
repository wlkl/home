import os
from flask import Flask, request, session, redirect, url_for, abort, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='abra-kadabra',
    USERNAME='wlkl',
    PASSWORD='wen1k0'
))


@app.route('/')
def show_picture():
    return render_template('show_picture.html')

@app.route('/new', methods=['POST'])
def create_picture():
    if not session.get('logged_in'):
        abort(401)



if __name__ == '__main__':
    app.run()
