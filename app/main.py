from data.productos import productos
from flask import Flask,render_template ,request,url_for,redirect,abort
from form import LoginForm
# Inicializamos la aplicación
app = Flask(__name__)
app.config['SECRET_KEY']='mi_clave_secreta_super_segura'

# Ruta 1: Devuelve un HTML muy básico
@app.route("/")
def home():
    return render_template('index.html')
#"""
#      <h1>¡Hola desde Flask en Docker!!!!</h1>
#        <p>Este es tu primer servidor Python funcionando.</p>
#    """
@app.route("/saludo/<name>")
def saludo(name):
    return render_template("saludo.html",name=name)
#f"<h1>Bienvenido a Flask, {name}!</h1>"


@app.route("/multiplicar/<int:a>/<int:b>")
def multiplicar(a, b):
    resultado = a * b
    return f"<h1>Multiplicar {a} x {b} es {resultado}</h1>"
@app.route("/catalogo/")
def catalogo():
    return render_template('catalogo.html',nombre="algo",listaDeproductos=productos)

@app.route("/catalogo/<int:idproducto>")   
def producto(idproducto):
#     if idproducto not in productos:
     if 0<=idproducto<len(producto):
         abort(404)
     return render_template("producto.html",idproducto=idproducto,producto=productos[idproducto])
    # Aquí podrías tener lógica para obtener datos de un catálogo, por ahora solo devolvemos un mensaje
@app.route("/contacto",methods=["GET"])
def contacto():
        return render_template('contacto.html')
@app.route("/contacto",methods=["POST"])
def contacto_post():
     nombre=request.form.get("nombre")
     mensaje=request.form.get("mensaje")
     return render_template("/contacto-data.html",nombre=nombre,mensaje=mensaje)
@app.route("/filtrar")
def filtrar():
     return render_template("filtrar.html")
@app.route("/filtrar-data",methods=["GET"])
def filtrar_data():
     precio_min=request.args.get("precio_min",type=float)
     precio_max=request.args.get("precio_max",type=float)
     productos_filtrados=[
          producto 
          for producto 
          in productos 
          if precio_min<= producto["precio"] <=precio_max
     ]
     return render_template("catalogo.html", nombre="filtrado",listaDeproductos=productos_filtrados)

@app.route("/login",methods=["GET","POST"])
def login():
     form=LoginForm()
     #validate_on_submit_ te valida si la peticion es POST y si se validan todos los campos
     if form.validate_on_submit():
          email=form.email.data
          password=form.password.data
          print(f"El usuario es {email} con la contraseña {password}")
          return redirect(url_for("gracias"))
     return render_template("login.html",form=form)
@app.route("/gracias")
def gracias():
     return render_template("gracias.html")
@app.errorhandler(404)
def pagina_no_encontrada(e):
     return render_template("404.html"),404
if __name__ == "__main__":
    # host='0.0.0.0' es VITAL en Docker para que el servidor sea accesible desde fuera del contenedor
    # debug=True hará que el servidor se reinicie automáticamente si cambias este archivo
    app.run(host="0.0.0.0", port=5000, debug=True)
