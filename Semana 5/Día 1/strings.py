
nombre = "Alex"
apellido = "Miller"
edad = 25

mensaje = "Hola como estás " + nombre + " " + apellido 
print(mensaje)

felicidades = "Felicidades, nos enteramos que hoy cumpliste " + str(edad) + " años."
print(felicidades)

formato_uno = f"Felicidades {nombre} {apellido}, nos enteramos que hoy cumpliste {edad} años."
print(formato_uno)

formato_dos = "Felicidades {} {}, nos enteramos que hoy cumpliste {} años.".format(nombre, apellido, edad)
print(formato_dos)

formato_tres = "Felicidades %s %s, nos enteramos que hoy cumpliste %d años." % (nombre, apellido, edad)
print(formato_tres)

print(len(mensaje))
print(mensaje.upper())