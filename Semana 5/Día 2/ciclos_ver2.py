nombres = ['Alex', 'Martha', 'Alan', 'Julieta', 'Roger']

for i in range(0, len(nombres)):
    print(nombres[i])
print('-----')
for nombre in nombres:
    print(nombre)


estudiante = {
    "nombre" : "Alex",
    "apellido" : "Miller",
    "edad" : 25,
    "curso" : "Python/Flask"
}
print('-----')
for propiedad in estudiante:
    print(propiedad, estudiante[propiedad])
print('-----')
for (propiedad, valor) in estudiante.items():
    print(propiedad, valor)

print('-----')
mensaje = "¡HOLA, ME GUSTA PROGRAMAR!"
for letra in mensaje:
    print(letra)