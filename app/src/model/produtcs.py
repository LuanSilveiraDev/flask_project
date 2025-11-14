from app import db, ma

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Cod_fabricante = db.Column(db.Integer)
    Ean = db.Column(db.BigInteger)
    Description_product = db.Column(db.String(50), nullable=False)
    cod_system = db.Column(db.Integer, nullable=False)
    Description_code_system = db.Column(db.String(50), nullable=False)
    
    def __init__(self, Cod_fabricante, Ean, Description_product, cod_system, Description_code_system):
        self.Cod_fabricante = Cod_fabricante
        self.Ean = Ean
        self.Description_product = Description_product
        self.cod_system = cod_system
        self.Description_code_system = Description_code_system
        
    def to_dict(self):
        return {
            "id": self.id,
            "Cod_fabricante": self.Cod_fabricante,
            "Ean": self.Ean,
            "Description_product": self.Description_product,
            "cod_system": self.cod_system,
            "Description_code_system": self.Description_code_system
        }

        
