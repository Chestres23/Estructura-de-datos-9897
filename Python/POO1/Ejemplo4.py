class Abuelo:

    def __init__(self, nombre, profesion, habilidad):
        self.nombre = nombre
        self.profesion = profesion
        self.habilidad = habilidad

    def realizaHabilidad (self):
        return (f"Yo puedo ", self.habilidad)

class Padre(Abuelo):
    def __init__(self, nombre, profesion, habilidad):
        super().__init__(nombre, profesion, habilidad)

    def realizaHabilidad (self):
        return (f"Yo puedo ", self.habilidad)

class Hijo(Padre):
    def __init__(self, nombre, profesion, habilidad):
        super().__init__(nombre, profesion, habilidad)

Jose = Hijo("Christian", "Desarrollador", "Cantar")
print(Jose.profesion)
print(Jose.habilidad)


