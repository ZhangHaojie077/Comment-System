# -*- coding: utf-8 -*-
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from comment_system import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password_hash = db.Column(db.String(128))
    token = db.Column(db.String(256))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

class Comment(db.Model):
    #__tablename__ = 'comment'
    id = db.Column(db.Integer)
    username = db.Column(db.String(30),primary_key=True)
    time = db.Column(db.String(20))
    blog_username = db.Column(db.String(30),primary_key=True)
    blog = db.Column(db.String(30),primary_key=True)
    content = db.Column(db.Text,primary_key=True)
    likes = db.Column(db.Integer)
    visible = db.Column(db.Boolean)

class Blog(db.Model):
    username = db.Column(db.String(30), primary_key=True)
    blog = db.Column(db.String(30),primary_key=True)
    date = db.Column(db.String(20),primary_key=True)
    flow = db.Column(db.Integer)
