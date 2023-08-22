from flask import Blueprint
#defino el odulo llamado mi blueprint
my_blueprint = Blueprint('blueprint'
                         ,__name__,
                         url_prefix='/blueprint')

#creo funcionalidad para el modulo
@my_blueprint.route("/ejemplo")
def ejemplo():
    return "este es el ejemplo"
