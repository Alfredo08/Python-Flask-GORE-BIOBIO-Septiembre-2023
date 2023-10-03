
estudiante = {
    "nombre" : "Alex",
    "apellido" : "Miller",
    "edad" : 25
}

print(estudiante)

estudiante["curso"] = "Python/Flask"
propiedad = "nombre"

print(estudiante[propiedad])

estudiante.pop('edad')
del estudiante['curso']
print(estudiante)


print(estudiante.keys())
print(estudiante.values())