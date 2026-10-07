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
    return f"<h1>Bienvenido a Flask, {name}!</h1>"

@app.route("/multiplicar/<int:a>/<int:b>")
def multiplicar(a, b):
    resultado = a * b
    return f"<h1>Multiplicar {a} x {b} es {resultado}</h1>"
@app.route("/catalogo/<int:id_producto>")
def catalogo(id_producto):
    productos=[
        {"nombre":"Teclado","precio": 29.99,"stock": 100,"disponible": True},
        {"nombre":"Mouse","precio": 19.99,"stock": 200,"disponible": True},
        {"nombre":"Monitor","precio": 199.99,"stock": 50,"disponible": False},
        {"nombre":"Auriculares","precio": 49.99,"stock": 150,"disponible": True},
        {"nombre":"Webcam","precio": 89.99,"stock": 75,"disponible": True},
        {"nombre":"Impresora","precio": 149.99,"stock": 30,"disponible": False},
        {"nombre":"Disco Duro Externo","precio": 79.99,"stock": 120,"disponible": True},
        {"nombre":"Memoria USB","precio": 14.99,"stock": 300,"disponible": True},
        {"nombre":"Router WiFi","precio": 59.99,"stock": 80,"disponible": True},
        {"nombre":"Altavoces Bluetooth","precio": 39.99,"stock": 90,"disponible": True}
    ]
    # Aquí podrías tener lógica para obtener datos de un catálogo, por ahora solo devolvemos un mensaje
    return render_template('catalogo.html',nombre="algo",id_producto=id_producto,listaDeproductos=productos)
if __name__ == "__main__":
    # host='0.0.0.0' es VITAL en Docker para que el servidor sea accesible desde fuera del contenedor
    # debug=True hará que el servidor se reinicie automáticamente si cambias este archivo
    app.run(host="0.0.0.0", port=5000, debug=True)
