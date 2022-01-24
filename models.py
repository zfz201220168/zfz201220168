from database import db


class Users(db.Model):  # 存储用户信息
    __tablename__ = 'users'  # the name of table

    username = db.Column(db.String(20), unique=True)
    ID = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(10))
    time = db.Column(db.DateTime)
    message = db.Column(db.String(20))
