from werkzeug.security import generate_password_hash
from flask import request, url_for, render_template, redirect
from app.src.model.users import Users, user_schema
from app import db

class ServicesRegister:
    
    @staticmethod
    def register_user():
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        email = request.form['email']

        pass_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
        user = Users(username, pass_hash, name, email)
        
        try:
            db.session.add(user)    
            db.session.commit()
            response = redirect(url_for('login'))
            return response
        except:
            db.session.rollback()
            return render_template('register.html', error="Registration failed. Please try again.") 

        
        