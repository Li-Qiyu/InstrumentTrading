from application import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, info='primary key')
    nickname = db.Column(db.String(30, 'utf8mb4_bin'), info='nickname')
    login_name = db.Column(db.String(20, 'utf8mb4_bin'), unique=True, info='login name')
    login_pwd = db.Column(db.String(32, 'utf8mb4_bin'), info='password')
    login_salt = db.Column(db.String(32, 'utf8mb4_bin'), info='random string')
    email = db.Column(db.String(50, 'utf8mb4_bin'), info='email')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='0:invalid; 1:valid')
    updated_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, server_default=db.FetchedValue())
