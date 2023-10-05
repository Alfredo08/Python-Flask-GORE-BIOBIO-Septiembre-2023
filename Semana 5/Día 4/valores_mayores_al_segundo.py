"""
Valores mayores que el segundo: escribe una función que acepte una lista y 
cree una nueva que contenga solo los valores de la lista original que sean 
mayores que su segundo valor. Imprime cuántos valores son y luego devuelve 
la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False

Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False
"""
def valores_mayores_al_segundo(lista):
    if len(lista) < 2:
        return False
    
    nueva_lista =[]
    for valor in lista:
        if valor > lista[1]:
            nueva_lista.append(valor)
    print(f"Son {len(nueva_lista)} valores mayores al segundo que es {lista[1]}")
    return nueva_lista

print(valores_mayores_al_segundo([5, 2, 3, 2, 1, 4]))
print(valores_mayores_al_segundo([5]))