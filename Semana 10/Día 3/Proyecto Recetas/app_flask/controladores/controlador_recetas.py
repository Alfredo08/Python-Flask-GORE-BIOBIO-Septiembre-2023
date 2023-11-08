from flask import render_template, request, redirect, session
from app_flask.modelos.modelo_recetas import Receta
from app_flask import app

@app.route('/recetas', methods=['get'])
def desplegar_recetas():
    if "id_usuario" not in session:
        return redirect('/')
    lista_recetas = Receta.obtener_todos()
    return render_template('recetas.html', lista_recetas = lista_recetas)

@app.route('/formulario/receta', methods=['GET'])
def desplegar_formulario_receta():
    if "id_usuario" not in session:
        return redirect('/')
    return render_template('formulario_receta.html')

@app.route('/crear/receta', methods=['POST'])
def crear_receta():
    if Receta.validar_receta(request.form) == False:
        return redirect('/formulario/receta')
    nueva_receta = {
        **request.form,
        "id_usuario": session['id_usuario']
    }
    Receta.crear_uno(nueva_receta)
    return redirect('/recetas')