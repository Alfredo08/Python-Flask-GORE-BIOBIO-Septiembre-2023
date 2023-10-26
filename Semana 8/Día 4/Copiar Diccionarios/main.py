estudiante = {
    "nombre" : "Alex",
    "apellido" : "Miller",
    "edad" : 25 
}

copia_estudiante = {
    **estudiante,
    "curso" : "Python/Flask",
    "edad" : 30
}

print(f"Estudiante {estudiante}")
print(f"Copia {copia_estudiante}")