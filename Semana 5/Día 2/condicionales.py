
# && || !
# and or not

calificacion = 6.8

if calificacion > 7.0:
    print("¡Felicidades, aprobaste el examen!")
else:
    print("Hay que tomar un segundo intento en el examen.")

lluvia = False
temperatura = 25

if lluvia == True and temperatura < 10:
    print("Trae tu paraguas y además un buen abrigo.")
elif lluvia == True:
    print("Solamente trae tu paraguas.")
else:
    print("Solamente trae un buen abrigo.")

"""
if lluvia == True and temperatura < 10:
    print("Trae tu paraguas y además un buen abrigo.")
else:
    if lluvia == True:
        print("Solamente trae tu paraguas.")
    else:
        print("Solamente trae un buen abrigo.")
"""