from flask import json, jsonify, request
from app_flask.modelos.modelo_recetas import Receta
from app_flask import app
from flask_cors import cross_origin


@app.route('/api/recetas', methods=['GET'])
@cross_origin(origins = ['http://127.0.0.1:5500'])
def api_obtener_todas():
    recetas = Receta.api_obtener_todos()
    return (jsonify(recetas), 200)

@app.route('/api/nueva/receta', methods=['POST'])
@cross_origin(origins = ['http://127.0.0.1:5500'])
def api_crear_receta():
    receta_nueva = json.loads(request.data.decode('utf-8'))
    Receta.crear_uno(receta_nueva)
    return (jsonify(receta_nueva), 201)