from app import app
from flask import jsonify, request, render_template
from app.src.services.auth.register import ServicesRegister
from app.src.services.auth.login import ServicesLogin
from app.src.model.users import Users
from app.src.services.register_products import ServicesProducts

@app.route('/', methods=['GET'])
@ServicesLogin.token_required 
def home(current_user):
        users = Users.query.filter_by(username=current_user.username).first()
        if users.has_permission('USER'):
            return render_template('navbar/navbar.html', user=current_user.username, users_USER=users.has_permission('USER'))
        elif users.has_permission('ADMIN'):
            return render_template('navbar/navbar.html', user=current_user.username, users_ADMIN=users.has_permission('ADMIN'))
        else :
            return render_template('navbar/navbar.html', user=current_user.username)
        
      

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return ServicesLogin.login() 
    return render_template('login.html')

@app.route('/logout', methods=['GET'])
def logout():
    return ServicesLogin.logout()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return ServicesRegister.register_user()
    return render_template('register.html')

@app.route('/product_register', methods=['POST'])
def product_register():
     return ServicesProducts.register_product()
 
@app.route('/list_products', methods=['GET'])
def list_products():
    return ServicesProducts.list_products()

@app.route('/product_register/<id>', methods=['PUT'])
def post_product(id):
    return ServicesProducts.update_products(id)
