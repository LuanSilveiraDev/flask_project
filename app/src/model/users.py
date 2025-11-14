import datetime
from app import db, ma

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())
    
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def has_permission(self, perm_name):
        return any(p.permission == perm_name for p in self.permissions)
    
class Permissions(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    permission = db.Column(db.String(50), nullable=False)
    user = db.relationship('Users', backref=db.backref('permissions', lazy=True))
    

    

class UserSchema(ma.Schema):
    class Meta:
        model = Users
        load_instance = True


user_schema = UserSchema()
users_schema = UserSchema(many=True)