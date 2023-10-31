from app_flask.config.mysqlconnection import connectToMySQL
from app_flask.modelos import modelo_quehaceres
from app_flask import BASE_DATOS, EMAIL_REGEX
from flask import flash

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
    
    @classmethod
    def crear_uno(cls, datos):
        query = """
                INSERT INTO usuarios(nombre, apellido, correo, password)
                VALUES (%(nombre)s, %(apellido)s, %(correo)s, %(password)s);
                """
        return connectToMySQL(BASE_DATOS).query_db(query, datos)

    @staticmethod
    def validar_login(datos):
        es_valido = True
        if datos == None:
            flash("Credenciales incorrectas", "error_login")
            es_valido = False
        return es_valido

    @staticmethod
    def validar_registro(datos):
        es_valido = True
        if len(datos['nombre']) <= 2:
            flash("Por favor proporciona tu nombre.", "error_nombre")
            es_valido = False
        if len(datos['apellido']) <= 2:
            flash("Por favor proporciona tu apellido.", "error_apellido")
            es_valido = False
        if len(datos['password']) < 8:
            flash("El password debe de tener al menos 8 caracteres.", "error_password")
            es_valido = False
        if datos['password'] != datos['password_confirmar']:
            flash("Tus password no coinciden.", "error_password")
            es_valido = False
        if not EMAIL_REGEX.match(datos['correo']):
            flash("Por favor proporciona un coreo válido.", "error_correo")
            es_valido = False
        return es_valido


