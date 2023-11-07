from flask import render_template, request, redirect, session
from app_flask import app

@app.route('/recetas', methods=['get'])
def desplegar_recetas():
    if "id_usuario" not in session:
        return redirect('/')
    return render_template('recetas.html')