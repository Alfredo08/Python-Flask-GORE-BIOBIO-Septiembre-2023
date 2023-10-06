
class Libro:
    # Constructor
    def __init__(self, titulo, autores, edicion, num_paginas, capitulos, idioma):
        # Atributos instancia
        self.titulo = titulo
        self.autores = autores
        self.edicion = edicion
        self.num_paginas = num_paginas
        self.capitulos = capitulos
        self.idioma = idioma
        self.cobertura = "Madera"

    # Métodos instancia
    def imprime_informacion(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autores: {self.autores}")
        print(f"Idioma: {self.idioma}")
        print(f"Num páginas: {self.num_paginas}")
        print(f"Tipo de cobertura: {self.cobertura}")
        return self

    def borra_informacion(self):
        self.titulo = None
        self.autores = None
        self.edicion = None
        self.num_paginas = None
        self.capitulos = None
        self.idioma = None
        self.cobertura = None
        return self

don_quijote = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 10, 1200, 50, "Español")
don_quijote.imprime_informacion().borra_informacion().imprime_informacion()

""" 
# Creando el objeto
don_quijote = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 10, 1200, 50, "Español")
don_quijote.imprime_informacion()
print('------')
el_principito = Libro("El Principito", "Antoine de Saint", 5, 300, 20, "Español")
el_principito.imprime_informacion()
print('------')
el_principito.num_paginas = 306
el_principito.cobertura = "Cartulina"
el_principito.imprime_informacion()
"""

