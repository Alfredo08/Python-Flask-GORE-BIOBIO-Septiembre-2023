
class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def imprime_fraccion(self):
        print(f"{self.numerador}/{self.denominador}")
    
    def suma_fraccion(self, fraccion_a_sumar):
        num_resultante = self.numerador * fraccion_a_sumar.denominador + fraccion_a_sumar.numerador * self.denominador
        den_resultante = self.denominador * fraccion_a_sumar.denominador
        nueva_fraccion = Fraccion(num_resultante, den_resultante)
        return nueva_fraccion

fraccion1 = Fraccion(2, 3)
fraccion2 = Fraccion(1, 2)
fraccion3 = Fraccion(3, 7)

fraccion1.imprime_fraccion()
fraccion2.imprime_fraccion()
fraccion3.imprime_fraccion()

resultado = fraccion1.suma_fraccion(fraccion2)
resultado.imprime_fraccion()
resultado2 = fraccion3.suma_fraccion(fraccion2)
resultado2.imprime_fraccion()
