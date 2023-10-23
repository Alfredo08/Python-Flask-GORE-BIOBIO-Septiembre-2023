from config.mysqlconnection import connectToMySQL

class Quehacer:
    def __init__(self, datos):
        self.id = datos['id']
        self.descripcion = datos['descripcion']
        self.status = datos['status']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']
        self.id_usuarios = datos['id_usuario']
    
    @classmethod
    def seleccionar_todos(cls):
        query = """
                SELECT *
                FROM quehaceres;
                """
        resultado = connectToMySQL('db_quehaceres').query_db(query)
        lista_quehaceres = []

        for renglon in resultado:
            quehacer = Quehacer(renglon)
            lista_quehaceres.append(quehacer)
        
        return lista_quehaceres




"""
SELECT *
seleccionar_todo()
get_all()

SELET *
WHERE id = id
seleccionar_uno(id)
get_one(id)

UPDATE 
WHERE id = id
actualizar_uno(id)
update_one(id)

DELETE
eliminar_uno(id)
delete_one(id)
"""