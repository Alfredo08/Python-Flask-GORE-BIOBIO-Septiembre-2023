from clases.persona import Persona

# Herencia, al poner el nombre de la clase 'padre'
class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, matricula, curso, calificacion):
        # Herencia, asignando los atributos de la clase 'padre'
        super().__init__(nombre, apellido, edad)
        self.matricula = matricula
        self.curso = curso
        self.calificacion = calificacion

    def imprime_informacion_estudiante(self):
        # Herencia, invocando el método heredado
        super().imprime_informacion()
        print(f"Matricula: {self.matricula}")
        print(f"Curso: {self.curso}")
        print(f"Calificacion: {self.calificacion}")

    # Polimorfismo, tenemos que implementar el método que no se implementó en la clase 'padre'
    def descansar(self):
        print("Como estudiante debes de descanzar al menos 8 horas, pero pudieras también lograrlo con 6")