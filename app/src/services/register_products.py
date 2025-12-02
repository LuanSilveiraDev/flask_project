from app.src.model.produtcs import Products
from flask import request, redirect, url_for, jsonify, render_template
from app import db
from sqlalchemy import or_

class ServicesProducts:
    @staticmethod
    def register_product():
        from sqlalchemy import or_
        
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
        

        Cod_fabricante = request.form['Cod_fabricante']
        Ean = request.form['Ean']
        Description_product = request.form['Description_product']
        cod_system = request.form['cod_system']
        Description_code_system = request.form['Description_code_system']
            
        Products.query.filter_by(id=id).update({
                'Cod_fabricante': Cod_fabricante,
                'Ean': Ean,
                'Description_product': Description_product,
                'cod_system': cod_system,
                'Description_code_system': Description_code_system,
        })
        db.session.commit()
        return redirect(url_for('list_products'))
   
    
    def remove_product(id):
        product_bd = Products.query.filter_by(id=id).first()
        db.session.delete(product_bd)
        db.session.commit()
        return redirect(url_for('list_products'))
    
    def search_products():
        dados = request.args.get('q', '').strip()
        page = request.args.get('page', 1, type=int)
        per_page = 13
        
        if dados:
            produtos = Products.query.filter(
                or_(
                    Products.Description_product.ilike(f"%{dados}%"),
                    Products.Ean.ilike(f"%{dados}%"),
                    Products.Cod_fabricante.ilike(f"%{dados}%"),
                    Products.cod_system.ilike(f"%{dados}%"),
                    Products.Description_code_system.ilike(f"%{dados}%")
                )
            ).paginate(page=page, per_page=per_page, error_out=False)
            
            return render_template('lista_produtos.html', produtos=produtos)
 
        
        return redirect(url_for('list_products'))