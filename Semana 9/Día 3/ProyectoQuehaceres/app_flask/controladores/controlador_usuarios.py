from flask import render_template, session, request, redirect, flash
from app_flask.modelos.modelo_usuarios import Usuario
from flask_bcrypt import Bcrypt
from app_flask import app

bcrypt = Bcrypt(app)

@app.route('/formulario/login', methods=['GET'])
@app.route('/login', methods=['GET'])
def desplegar_login():
    return render_template('login.html')

@app.route('/procesa/login', methods=['POST'])
def procesa_login():
    usuario_login = {
        "correo" : request.form["correo"]
    }

    usuario = Usuario.obtener_uno(usuario_login)

    if Usuario.validar_login(usuario) == False:
        return redirect('/login')
                                    # password encriptado, password del formulario
    if not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash('Credenciales invalidas', 'error_login')
        return redirect('/login')

    session["nombre"] = usuario.nombre
    session["apellido"] = usuario.apellido
    session["id_usuario"] = usuario.id

    return redirect('/quehaceres')

@app.route('/procesa/registro', methods=['POST'])
def procesa_registro():
    if Usuario.validar_registro(request.form) == False:
        return redirect('/login')

    password_encriptado = bcrypt.generate_password_hash(request.form['password'])
    usuario_nuevo = {
        **request.form,
        'password' : password_encriptado
    }

    id_usuario = Usuario.crear_uno(usuario_nuevo)
    session["nombre"] = request.form['nombre']
    session["apellido"] = request.form['apellido']
    session["id_usuario"] = id_usuario
    return redirect('/quehaceres')
    
    

@app.route('/procesa/logout', methods=['POST'])
def procesa_logout():
    session.clear()
    return redirect('/login')

@app.route('/usuario_quehaceres', methods=['GET'])
def obtener_usuario_con_quehaceres():
    datos = {
        'id' : session['id_usuario']
    }
    usuario = Usuario.onbtener_uno_con_quehaceres(datos)
    existen_quehaceres = True

    if len(usuario.lista_quehaceres) == 0:
        existen_quehaceres = False

    return render_template('usuario_quehacer.html', usuario = usuario, existen_quehaceres=existen_quehaceres)