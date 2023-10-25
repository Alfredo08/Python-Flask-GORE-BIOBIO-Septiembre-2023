from flask import render_template, session, request, redirect
from app_flask.modelos.modelo_usuarios import Usuario
from app_flask import app

@app.route('/formulario/login', methods=['GET'])
@app.route('/login', methods=['GET'])
def desplegar_login():
    return render_template('login.html')

@app.route('/procesa/login', methods=['POST'])
def procesa_login():
    usuario_login = {
        "correo" : request.form["correo"],
        "password" : request.form["password"]
    }

    usuario = Usuario.obtener_uno(usuario_login)

    if usuario == None:
        print(f'Este usuario no existe: {usuario_login["correo"]} {usuario_login["password"]}')
        return redirect('/login')
    
    session["nombre"] = usuario.nombre
    session["apellido"] = usuario.apellido
    session["id_usuario"] = usuario.id

    return redirect('/quehaceres')



@app.route('/procesa/logout', methods=['POST'])
def procesa_logout():
    session.clear()
    return redirect('/login')