from flask import render_template, session, request, redirect
from app_flask.modelos.modelo_quehaceres import Quehacer
from app_flask import app

@app.route('/quehaceres', methods=['GET'])
def obtener_quehaceres():
    if "nombre" not in session:
        return redirect('/login')
    lista_quehaceres_objetos = Quehacer.seleccionar_todos()
    return render_template('quehaceres.html', lista_quehaceres=lista_quehaceres_objetos)

@app.route('/formulario/quehacer', methods=['GET'])
def desplegar_formulario_quehacer():
    if "nombre" not in session:
        return redirect('/login')
    return render_template('formulario_quehacer.html')

@app.route('/nuevo/quehacer', methods=['POST'])
def crear_quehacer():
    quehacer_nuevo = {
        "id_usuario" : session['id_usuario'],
        "descripcion" : request.form["descripcion"],
        "status" : request.form["status"]
    }
    id_nuevo_quehacer = Quehacer.agregar_uno(quehacer_nuevo)

    return redirect('/quehaceres')

@app.route('/eliminar/quehacer/<int:id>', methods=['POST'])
def eliminar_quehacer(id):
    datos = {
        "id" : id
    }
    Quehacer.eliminar_uno(datos)
    return redirect('/quehaceres')

@app.route('/formulario/editar/quehacer/<int:id>', methods=['GET'])
def formulario_editar_quehacer(id):
    datos = {
        "id" : id
    }
    quehacer = Quehacer.seleccionar_uno(datos)
    return render_template("formulario_editar_quehacer.html", quehacer=quehacer)

@app.route('/editar/quehacer/<int:id>', methods=['POST'])
def editar_quehacer(id):
    datos = {
        "id" : id,
        "descripcion" : request.form['descripcion'],
        "status" : request.form['status']
    }
    Quehacer.editar_uno(datos)
    return redirect('/quehaceres')


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