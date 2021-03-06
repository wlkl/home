import os
from flask import Flask

app = Flask(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'home.db'),
    DEBUG=True,
    SECRET_KEY='abra-kadabra',
))

from home.database import db_session


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


from home.helper import correct_bd

correct_bd()

import home.routes
