nombres = ['Alex', 'Martha', 'Alan', 'Roger', 'Julieta']
nombre = 'Martin'

def agrega_nombre(lista_nombres, nuevo_nombre):
    lista_nombres.append(nuevo_nombre)
    nuevo_nombre = 'Humberto'
    return None

agrega_nombre(nombres, nombre)
print(nombres)
print(nombre)


def agrega_propiedad(diccionario, propiedad, valor):
    diccionario[propiedad] = valor
    print(f"Se ha agregado la propiedad '{propiedad}' con valor '{valor}' al diccionario.")

estudiante = {
    "nombre" : "Alex",
    "apellido" : "Miller",
    "edad" : 25
}

agrega_propiedad(estudiante, 'curso', 'Python/Flask')
print(estudiante)