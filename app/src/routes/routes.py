from app import app
from flask import jsonify, request, render_template
from app.src.services.auth.register import ServicesRegister
from app.src.services.auth.login import ServicesLogin
from app.src.model.users import Users
from app.src.services.register_products import ServicesProducts, Products

@app.route('/', methods=['GET'])
@ServicesLogin.token_required 
def home(current_user):
    return render_template('perfil.html', usuario=current_user)
      

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

@app.route('/product_register', methods=['GET', 'POST'])
def product_register():
     if request.method == 'POST':
        return ServicesProducts.register_product()
     return render_template('register_products.html')
 
@app.route('/list_products', methods=['GET'])
def list_products():
    if request.method == 'GET':
        return ServicesProducts.list_products()
    return render_template('lista_produtos.html')

@app.route('/<int:id>/update_product', methods=['GET','POST'])
def update_product(id):
    if request.method == 'POST':
        return ServicesProducts.update_products(id)
    
    product_bd = Products.query.get(id)
    return render_template('update_product.html', produtos=product_bd)

@app.route('/<int:id>/delete_product')
def delete_product(id):
    return ServicesProducts.remove_product(id)

@app.route('/search_products', methods=['GET'])
def search_products():
    return ServicesProducts.search_products()
    
