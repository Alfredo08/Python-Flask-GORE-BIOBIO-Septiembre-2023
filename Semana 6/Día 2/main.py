from clases.persona import Persona
from clases.estudiante import Estudiante

alex = Persona("Alex", "Miller", 25)
alex.imprime_informacion()

martha = Estudiante("Martha", "Gomez", 22, 12323, "Python/Flask", 8.9)

martha.imprime_informacion()

martha.descansar()
