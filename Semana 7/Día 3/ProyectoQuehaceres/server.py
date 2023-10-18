from flask import Flask, render_template

app = Flask(__name__)

lista_usuarios = ["Alex Miller", "Martha Gómez", "Roger Anderson", "Julieta Venegas"]

# http://127.0.0.1:5000/mensaje
@app.route('/mensaje', methods=['GET'])
def mensaje():
    return "<h1> ¡Hola clase! ¡Bienvenidos a su primer servidor y su primera ruta! </h1>"

@app.route('/bienvenida/<string:nombre>/<string:apellido>/<int:edad>', methods=['GET'])
def bienvenida(nombre, apellido, edad):
    print(f"{nombre} {apellido} {edad}")
    print(edad + 5)
    return f"Te damos la bienvenida {nombre} {apellido}."

@app.route('/home/<string:nombre>', methods=['GET'])
def home(nombre):
    return render_template('index.html', usuarios=lista_usuarios, clase="Clase de Python/Flask", nombre=nombre)

if __name__ == "__main__":
    app.run(debug=True)