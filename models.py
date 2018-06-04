from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Blog(Base):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    catagory = Column(String(50))
    auther = Column(String(50))
    content = Column(Text)
    post_date = Column(DateTime, default=datetime.now)

    def __reqr__(self):
        return "<Blog %r>" % self.title
