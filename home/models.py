from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.orm import mapper
from home.database import metadata, db_session
from werkzeug.security import generate_password_hash, check_password_hash


class User(object):
    query = db_session.query_property()

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return 'username %r' % self.name


users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50), unique=True),
    Column('email', String(120), unique=True),
    Column('password', String(250))
    )

mapper(User, users)


class Image(object):
    query = db_session.query_property()

    def __init__(self, image=None):
        self.image = image

    def __repr__(self):
        return self.image


images = Table('images', metadata,
               Column('id', Integer, primary_key=True),
               Column('image', String(30), unique=True))

mapper(Image, images)