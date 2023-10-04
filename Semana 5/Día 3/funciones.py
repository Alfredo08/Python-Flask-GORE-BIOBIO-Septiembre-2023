
def agrega_dos_numeros(num1 = 0, num2 = 0):
    total = num1 + num2
    return total

def imprime_informacion(nombre = "", apellido = "", calificacion = 0.0):
    print(f"Hola {nombre} {apellido}. Bienvenido al curso de python.")
    print(f"Tu calificación en el examen es de {calificacion}")

resultado = agrega_dos_numeros(20, 30)
print(resultado)

resultado2 = agrega_dos_numeros(20)
print(resultado2)

resultado3 = agrega_dos_numeros()
print(resultado3)

imprime_informacion(calificacion = 9.8, nombre = 'Alex', apellido = 'Miller')
