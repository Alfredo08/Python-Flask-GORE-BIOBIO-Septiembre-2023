from app_flask.config.mysqlconnection import connectToMySQL
from app_flask.modelos import modelo_usuarios
from flask import flash
from app_flask import BASE_DATOS

class Receta:
    def __init__(self, datos):
        self.id = datos['id'] 
        self.nombre = datos['nombre']
        self.descripcion = datos['descripcion']
        self.instrucciones = datos['instrucciones']
        self.fecha_coccion = datos['fecha_coccion']
        self.menos_30 = datos['menos_30']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']
        self.id_usuario = datos['id_usuario']
        self.usuario = None
    
    @classmethod
    def crear_uno(cls, datos):
        query = """
                INSERT INTO recetas(nombre, descripcion, instrucciones, fecha_coccion, menos_30, id_usuario)
                VALUES (%(nombre)s, %(descripcion)s, %(instrucciones)s, %(fecha_coccion)s, %(menos_30)s, %(id_usuario)s);
                """
        return connectToMySQL(BASE_DATOS).query_db(query, datos)
    
    @classmethod
    def obtener_todos(cls):
        query = """
                SELECT *
                FROM recetas JOIn usuarios
                    ON recetas.id_usuario = usuarios.id;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query)
        lista_recetas = []
        for renglon in resultado:
            receta_actual = cls(renglon)
            usuario = {
                **renglon,
                'nombre' : renglon['usuarios.nombre'],
                'id' : renglon['usuarios.id'],
                'fecha_creacion' : renglon['usuarios.fecha_creacion'],
                'fecha_actualizacion' : renglon['usuarios.fecha_actualizacion']
            }
            receta_actual.usuario = modelo_usuarios.Usuario(usuario)
            lista_recetas.append(receta_actual)
        return lista_recetas

    @staticmethod
    def validar_receta(datos):
        es_valido = True
        if len(datos['nombre']) < 3:
            flash('Por favor proporciona el nombre de la receta.', 'error_nombre')
            es_valido = False
        if len(datos['descripcion']) < 3:
            flash('Por favor proporciona la descripcion de la receta.', 'error_descripcion')
            es_valido = False
        if len(datos['instrucciones']) < 3:
            flash('Por favor proporciona las instrucciones de la receta.', 'error_instrucciones')
            es_valido = False
        if datos['fecha_coccion'] == '':
            flash('Por favor proporciona la fecha de cocción.', 'error_fecha_coccion')
            es_valido = False
        if "menos_30" not in datos:
            flash('Por favor seleccion si la receta necesita menos de 30 minutos o mas', 'error_menos_30')
            es_valido = False
        return es_valido
    
    # Métodos para las rutas /api
    @classmethod
    def api_obtener_todos(cls):
        query = """
                SELECT *
                FROM recetas
                """
        return connectToMySQL(BASE_DATOS).query_db(query)