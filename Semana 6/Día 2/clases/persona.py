
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def imprime_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        return self
    
    # Polimorfismo, dejar sin implementación un método
    def descansar(self):
        raise NotImplementedError
    

