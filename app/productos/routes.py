from flask import render_template
from . import productos 
import app 
from .forms import RegistrarProductoForm
#rutas del modulo "productos"
@productos.route("/listar")
def listar():
    
    #Se listan los productos
    #modelos
    productos = app.models.Producto.query.all()
    return render_template ("index.html",
                            productos = productos)

@productos.route("/nuevo", 
                 methods = ["GET", "POST"])
def nuevo():
    #Registrar formulario
    form = RegistrarProductoForm()
    
    #definir objeto
    p = app.models.Producto()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit( )
        return "Producto registrado" 
    return render_template("new.html",
                           form = form)