"""
Primero más longitud: crea una función que acepte una lista y devuelva 
la suma del primer valor de la lista, más la longitud de la lista.

Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)
"""
def primero_mas_longitud(lista):
    suma = lista[0] + len(lista)
    return suma

print(primero_mas_longitud([10, 20, 30, 40]))
print(primero_mas_longitud([-2, -5, -7, -9, -11]))