import os
from home.database import db_session
from home import app
from home.models import Image

def correct_bd():
    db_session.query(Image).delete()
    db_session.commit()
    for name in os.listdir(app.static_folder):
        db_session.add(Image(name))
    db_session.commit()
    response = db_session.query(Image).all()
    return response
