from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from .my_blueprint import my_blueprint
from app.productos import productos


#   Regisrar el nuevo modulo
app = Flask(__name__)
app.register_blueprint(my_blueprint)
app.register_blueprint(productos)

# crear el objeto de aplicación
app.config.from_object(Config)

# crear el objeto sqlalchemy
db = SQLAlchemy(app)

#crear el objeto de migracion y activarlo
migrate = Migrate(app , db)

#Configuracion bootstrap
bootstrap = Bootstrap(app)


#traer los modelos
from .models import Producto,Cliente,Venta,Detalle
