from application import db
from flask import Blueprint, render_template, request, url_for, redirect, session, escape, flash

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(30, 'utf8mb4_bin'), unique=True)
    username = db.Column(db.String(20, 'utf8mb4_bin'), unique=True)
    password = db.Column(db.String(32, 'utf8mb4_bin'))
    login_salt = db.Column(db.String(32, 'utf8mb4_bin'))
    email = db.Column(db.String(50, 'utf8mb4_bin'))
    admin = db.Column(db.String(50),default='no')
    status = db.Column(db.Integer, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, server_default=db.FetchedValue())

    def __init__(self, nickname, username, password, email, admin):
        self.nickname = nickname
        self.username = username
        self.password = password
        self.email = email
        self.admin = admin

    def __repr__(self):
        return "%s" % self.username

    def addUser(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 1

    def isExisted(self):
        temUser = User.query.filter_by(username=self.username, password=self.password).first()
        if temUser is None:
            return 0
        else:
            return 1


def findUser(username):
    ID = User.query.filter_by(username=username).first()
    return ID


def delUser(username):
    user = User.query.filter(User.username==username).first()
    db.session.delete(User)
    db.session.commit()
    return 1


def getAllUser():
    Userlist = User.query.all()
    return Userlist


def getNickname(username):
    Username = User.query.filter(User.username==username).first()
    nickname = Username.nickname
    return nickname


def getAdmin():
    adminList = User.query.filter(User.admin=="yes").all()
    return adminList


def modifyUser(username,password,email):
    user = User.query.filter_by(username=username).first()
    user.password = password
    user.email = email
    db.session.commit()
    return 1