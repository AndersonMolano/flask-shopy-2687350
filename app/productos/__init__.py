#Depenedencias
from flask import Blueprint
productos = Blueprint('productos',
                                __name__,
                                url_prefix = '/productos',
                                template_folder = 'templates')
#Relacion del archivo de rutas:
from . import routes 
