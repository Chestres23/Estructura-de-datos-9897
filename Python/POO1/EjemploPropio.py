class Yo:
    def __init__(self,name, edad, carrera, habilidad):
        self.name = name
        self.edad = edad
        self.carrera = carrera
        self.habilidad = habilidad

    def __str__(self):
        return f"Me llamo {self.name}, tengo {self.edad} años de edad y sigo la carrera de {self.carrera} y tengo la habilidad de {self.habilidad}"

    def Yo(self):
        print(f"{Christian} ")

person_1 = Yo("Christian", 19,"Ing. en TICS","tocar la guitarra" )

print(person_1)
#help(Yo)

