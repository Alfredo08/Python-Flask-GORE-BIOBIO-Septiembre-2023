from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secreto"

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

lista_usuarios = [{
    "id" : 1,
    "nombre" : "Alex",
    "apellido" : "Miller",
    "correo" : "alex@miller.com",
    "password" : "pass123"
},
{
    "id" : 2,
    "nombre" : "Martha",
    "apellido" : "Gómez",
    "correo" : "martha@gomez.com",
    "password" : "pass123"
}]

@app.route('/quehaceres', methods=['GET'])
def obtener_quehaceres():
    if "nombre" not in session:
        return redirect('/login')
    return render_template('quehaceres.html', lista_quehaceres=lista_quehaceres)

@app.route('/formulario/quehacer', methods=['GET'])
def desplegar_formulario_quehacer():
    if "nombre" not in session:
        return redirect('/login')
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

@app.route('/formulario/login', methods=['GET'])
@app.route('/login', methods=['GET'])
def desplegar_login():
    return render_template('login.html')

@app.route('/procesa/login', methods=['POST'])
def procesa_login():
    correo = request.form["correo"]
    password = request.form["password"]

    for usuario in lista_usuarios:
        if usuario["correo"] == correo and usuario["password"] == password:
            session["nombre"] = usuario["nombre"]
            session["apellido"] = usuario["apellido"]
            session["id_usuario"] = usuario["id"]

            return redirect('/quehaceres')

    print(f'Este usuario no existe: {correo} {password}')
    return redirect('/login')

@app.route('/procesa/logout', methods=['POST'])
def procesa_logout():
    session.clear()
    return redirect('/login')

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