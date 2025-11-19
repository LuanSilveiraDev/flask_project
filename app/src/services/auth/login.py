from werkzeug.security import check_password_hash
from app.src.model.users import Users
from flask import jsonify, request, url_for, render_template, redirect
import jwt
from app import app
from functools import wraps
from app.src.repository.users_repository import user_by_username
import datetime

class ServicesLogin:
    @staticmethod
    def login():
        
        username = request.form['username']
        password = request.form['password']
        # auth = request.authorization
        user = Users.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            token = jwt.encode({"username": user.username, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)}, app.config['SECRET_KEY'], algorithm='HS256')
            response = redirect(url_for('home'))
            response.set_cookie('token', token, httponly=True, secure=True, samesite='Lax')
            return response
        return render_template('navbar/navbar.html')
    
    @app.context_processor
    def inject_user():
        token = request.cookies.get('token')
        if not token:
            return {'current_user': None}
        else:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            return {'current_user': data['username']}
    


    @staticmethod
    def logout():
        response = redirect(url_for('login'))
        response.delete_cookie('token', httponly=True, secure=True, samesite='Lax')
        return response

    @staticmethod
    def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.cookies.get('token')
            if not token:
                return jsonify({'message': 'token is missing', 'data': {}}), 401
            try:
                data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
                current_user = user_by_username(username=data['username'])
            except:
                return jsonify({'message': 'token is invalid or expired', 'data': {}}), 401
            return f(current_user, *args, **kwargs)
        return decorated


