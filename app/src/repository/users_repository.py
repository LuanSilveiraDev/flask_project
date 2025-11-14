from app.src.model.users import Users

def user_by_username(username):
        try:
            return Users.query.filter(Users.username == username).one()
        except:
            return None
    
    