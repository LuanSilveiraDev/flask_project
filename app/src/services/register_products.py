from app.src.model.produtcs import Products
from flask import request, jsonify
from app import db

class ServicesProducts:
    @staticmethod
    def register_product():
        
        data = request.get_json()
        
        Cod_fabricante = data['Cod_fabricante']
        Ean = data['Ean']
        Description_product = data['Description_product']
        cod_system = data['cod_system']
        Description_code_system = data['Description_code_system']

        products = Products(Cod_fabricante, Ean, Description_product, cod_system, Description_code_system)

        
        try:
            db.session.add(products)
            db.session.commit()
            return jsonify({"Cod_Fabricanmte": Cod_fabricante}), 200
        except:
            return jsonify({"Error": "Request not found"}), 400
        
    @staticmethod
    def list_products():
        products = Products.query.all()
        data = [prod.to_dict() for prod in products]
        return jsonify(data), 200
    
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