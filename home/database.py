from home import app
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
#from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///' + app.config['DATABASE'], convert_unicode=True)
metadata = MetaData()
#metadata.reflect(extend_existing=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

def init_db():
    metadata.create_all(bind=engine)