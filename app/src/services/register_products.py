from app.src.model.produtcs import Products
from flask import request, redirect, url_for, jsonify, render_template
from app import db

class ServicesProducts:
    @staticmethod
    def register_product():
        
        
        Cod_fabricante = request.form['Cod_fabricante']
        Ean = request.form['Ean']
        Description_product = request.form['Description_product']
        cod_system = request.form['cod_system']
        Description_code_system = request.form['Description_code_system']

        products = Products(Cod_fabricante, Ean, Description_product, cod_system, Description_code_system)

        
        try:
            db.session.add(products)
            db.session.commit()
            response = redirect(url_for('product_register'))
            return response
        except:
            return jsonify({"Error": "Request not found"}), 400
        
    @staticmethod
    def list_products():
        page = request.args.get('page', 1, type=int)
        per_page = 13
        products = Products.query.paginate(page=page, per_page=per_page)
        return render_template (
            "lista_produtos.html",
            produtos=products
        )
    
    @staticmethod
    def update_products(id):
        data = request.get_json()
        
        Cod_fabricante = data['Cod_fabricante']
        Ean = data['Ean']
        Description_product = data['Description_product']
        cod_system = data['cod_system']
        Description_code_system = data['Description_code_system']
        
        product = Products.query.get(id)
        
        if not product:
            return jsonify({'message': 'product don"t exist', 'data': {}}), 404
        
        try:
            product.Cod_fabricante = Cod_fabricante
            product.Ean = Ean
            product.Description_product = Description_product
            product.cod_system = cod_system
            product.Description_code_system = Description_code_system
            db.session.commit()
            return jsonify({"Product Update": "Sucessuful"}), 201
        except:
            return jsonify({"Erro": "Product not found"}), 500