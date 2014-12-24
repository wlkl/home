from home import app
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///' + app.config['DATABASE'], convert_unicode=True)
metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


def init_db():
    metadata.bind = engine
    metadata.reflect(extend_existing=True)
    metadata.create_all()


