from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


engine = create_engine(
    'mysql+pymysql://root:1234@localhost/test?charset=utf8',
    convert_unicode=True)
session = sessionmaker(bind=engine)


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import Blog
    Base.metadata.create_all(Blog, bind=engine)
