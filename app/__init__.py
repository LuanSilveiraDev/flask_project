from flask import Flask
from app.data.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os

app = Flask(__name__,
            template_folder="src/view/templates")
app.config.from_object(Config)
db = SQLAlchemy(app)
ma = Marshmallow(app)

from app.src.model import users
from app.src.routes import routes   

with app.app_context():
    db.create_all()
    print("Sucesso")

if __name__ == '__main__':
    app.run(debug=True ,host='0.0.0.0', port=5000 )
    
