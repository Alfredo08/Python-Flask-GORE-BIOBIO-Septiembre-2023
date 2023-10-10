import random

class Fraccion:
    curso = "Python/Flask"
    lista_fracciones = []

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
        Fraccion.lista_fracciones.append(self);
    
    def imprime_fraccion(self):
        print(f"{self.numerador}/{self.denominador}")
    
    def suma_fraccion(self, fraccion_a_sumar):
        num_resultante = self.numerador * fraccion_a_sumar.denominador + fraccion_a_sumar.numerador * self.denominador
        den_resultante = self.denominador * fraccion_a_sumar.denominador
        nueva_fraccion = Fraccion(num_resultante, den_resultante)
        return nueva_fraccion
    
    @classmethod
    def imprime_todas_las_fracciones(cls):
        for fraccion in cls.lista_fracciones:
            fraccion.imprime_fraccion()

    @classmethod
    def encuentra_fraccion_con_denominador(cls, den):
        for fraccion in cls.lista_fracciones:
            if fraccion.denominador == den:
                fraccion.imprime_fraccion()

    @staticmethod
    def suma_dos_numeros(num1, num2):
        total = num1 + num2
        return total

resultado = Fraccion.suma_dos_numeros(10, 20)
print(resultado)
"""
for i in range(20):
    num = random.randint(1, 11)
    den = random.randint(1, 11)
    nueva_fraccion = Fraccion(num, den)

Fraccion.curso = "Fundamentos de la web"

Fraccion.imprime_todas_las_fracciones()

print("-------")

Fraccion.encuentra_fraccion_con_denominador(2)
"""