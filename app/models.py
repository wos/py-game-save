from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50), unique=False)

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.username)

class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    color = Column(String(10), unique=False)
    text = Column(String(120), unique=False)

    def __init__(self, name=None, color=None, text=None):
        self.name = name
        self.color = color
        self.text = text

    def __repr__(self):
        return '<Card %r>' % (self.name)