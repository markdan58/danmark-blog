from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    

    @property
    def password(self):
        raise AttributeError('This password is inaccessible')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'



class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class Comment(db.Model):
    '''
    Class Comments for the Comments column
    '''
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comments = db.Column(db.String(255))
    date_created = db.Column(db.Date, default=datetime.now)
    Newblog_id = db.Column(db.Integer, db.ForeignKey("Newblog.id"))




class Newblog(db.Model):
    '''
    Class pitch that defines the tables in the pitch database
    '''

    newblog_list = []
    __tablename__ = 'Newblog'

    id = db.Column(db.Integer,primary_key = True)
    actual_blog = db.Column(db.String(255))
    vote_count = db.Column(db.String)
    title = db.Column(db.String(255))
    published_On = db.Column(db.Date, default=datetime.now)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    Newblog = db.relationship('Comment',backref = 'Newblog',lazy = "dynamic")


    '''
    Function that saves new created pitches
    '''
    def save_Newbolg(self):
        db.session.add(self)
        db.session.commit()