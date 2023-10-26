from app_flask.config.mysqlconnection import connectToMySQL
from app_flask.modelos import modelo_quehaceres
from app_flask import BASE_DATOS

class Usuario:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.password = datos['password']
        self.correo = datos['correo']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']
        self.lista_quehaceres = []
    
    @classmethod
    def obtener_uno(cls, datos):
        query = """
                SELECT *
                FROM usuarios
                WHERE correo = %(correo)s AND password = %(password)s;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, datos)
        if len(resultado) == 0:
            return None
        usuario = Usuario(resultado[0])
        return usuario

    @classmethod
    def onbtener_uno_con_quehaceres(cls, datos):
        query = """
                SELECT *
                FROM usuarios u LEFT JOIN quehaceres q
                    ON u.id = q.id_usuario
                WHERE u.id = %(id)s;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, datos)

        usuario_actual = Usuario(resultado[0])

        for renglon in resultado:
            if renglon['descripcion'] != None:
                quehacer = {
                    **renglon,
                    "id" : renglon['q.id'],
                    "fecha_creacion" : renglon['q.fecha_creacion'],
                    "fecha_actualizacion" : renglon['q.fecha_actualizacion']
                }
                quehacer_actual = modelo_quehaceres.Quehacer(quehacer)
                usuario_actual.lista_quehaceres.append(quehacer_actual)
        return usuario_actual

