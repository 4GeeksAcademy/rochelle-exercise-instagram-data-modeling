import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'

    id = Column(Integer, primary_key=True)
    followed_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('user', uselist=False, back_populates='follower')

    def serialize(follower):
        return {
            "follower id": follower.id,
            "followed id": follower.followed_id
        }

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    post = relationship('post', uselist=False, back_populates='user')

    def serialize(user):
        return {
            "id": user.id,
            "username": user.username,
            "first name": user.first_name,
            "last name": user.last_name,
            "email": user.email
        }

class Post(Base):
    __tablename__ = 'post'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    text = Column(String(250))
    comment = relationship('comment', uselist=False, back_populates='post')

    def serialize(post):
        return {
            "id": post.id,
            "user id": post.user_id,
            "text": post.text
        }

class Comment(Base):
    __tablename__ = 'comment'
    
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer)
    post_id = Column(Integer, ForeignKey('post.id'))
    text = Column(String(250), nullable=False)
    post = relationship('post', uselist=False, back_populates='comment')

    def serialize(comment):
        return {
            "id": comment.id,
            "author id": comment.author_id,
            "post id": comment.post_id,
            "text": comment.text
        }

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
