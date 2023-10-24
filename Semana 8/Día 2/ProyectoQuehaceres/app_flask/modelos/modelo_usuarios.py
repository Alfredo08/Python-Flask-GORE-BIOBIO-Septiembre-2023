from app_flask.config.mysqlconnection import connectToMySQL
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
