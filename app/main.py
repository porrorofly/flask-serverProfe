from data.productos import productos
from flask import Flask,render_template 

# Inicializamos la aplicación
app = Flask(__name__)


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
    return render_template("producto.html",idproducto=idproducto,producto=productos[idproducto])
    # Aquí podrías tener lógica para obtener datos de un catálogo, por ahora solo devolvemos un mensaje
if __name__ == "__main__":
    # host='0.0.0.0' es VITAL en Docker para que el servidor sea accesible desde fuera del contenedor
    # debug=True hará que el servidor se reinicie automáticamente si cambias este archivo
    app.run(host="0.0.0.0", port=5000, debug=True)
