from flask import Flask, render_template, request, redirect

app = Flask(__name__)

lista_usuarios = ["Alex Miller", "Martha Gómez", "Roger Anderson", "Julieta Venegas"]

lista_quehaceres = [{
    "id": 1,
    "descripcion": "Aprender SQL",
    "status": "completo"
},
{
    "id": 2,
    "descripcion": "Aprender Lenguaje Python",
    "status": "completo"
},
{
    "id": 3,
    "descripcion": "Aprender Flask",
    "status": "en_proceso"
}]

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

@app.route('/quehaceres', methods=['GET'])
def obtener_quehaceres():
    return render_template('quehaceres.html', lista_quehaceres=lista_quehaceres)

@app.route('/formulario/quehacer', methods=['GET'])
def desplegar_formulario_quehacer():
    return render_template('formulario_quehacer.html')

@app.route('/nuevo/quehacer', methods=['POST'])
def crear_quehacer():
    quehacer_nuevo = {
        "id" : request.form["id"],
        "descripcion" : request.form["descripcion"],
        "status" : request.form["status"]
    }
    lista_quehaceres.append(quehacer_nuevo)

    return redirect('/quehaceres')

if __name__ == "__main__":
    app.run(debug=True)


"""
GET
Obtener toda la tabla/lista de nuestra base de datos
URL: '/quehaceres'
Funcion:
    obtener_quehaceres()
    get_quehaceres()
    get_todos_quehaceres()

Obtener un solo elemento de la tabla/lista de nuestra base de datos
URL: '/quehacer/<int:id>'
Funcion:
    obtener_quehacer(id)
    get_quehacer(id)

Desplegar el formulario que eventualmente estará conectado con una tabla/lista de nuestra base de datos
URL: /formulario/quehacer
Funcion:
    desplegar_formulario_quehacer()

POST
Agregar un nuevo elemento a la tabla/lista de nuestra base de datos
URL: /nuevo/quehacer
Funcion:
    crear_quehacer()
    nuevo_quehacer()
    agregar_quehacer()

PUT - Utilizar el método POST
Editar un elemento existente en la tabla/lista de nuestra base de datos
URL: /editar/quehacer/<int:id>
     /actualizar/quehacer/<int:id>
Funcion:
    editar_quehacer(id)
    actualizar_quehacer(id)

DELETE - Utilizar el método POST
Eliminar un elemento existente en la table/lista de nuestra base de datos
URL: /eliminar/quehacer/<int:id>
     /remover/quehacer/<int:id>
Funcion:
    remover_quehacer(id)
    eliminar_quehacer(id)

"""