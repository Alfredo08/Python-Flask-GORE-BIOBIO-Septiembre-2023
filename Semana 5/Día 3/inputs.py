
nombres = []
opcion = input("1) Agregar nombre \n2) Mostrar la lista \n3) Terminar \n")

while opcion != '3':
    if opcion == '1':
        nombre = input("¿Cuál es el nombre que quieres agregar a la lista? ")
        nombres.append(nombre)

    if opcion == '2':
        print(nombres)
        
    opcion = input("1) Agregar nombre \n2) Mostrar la lista \n3) Terminar \n")

