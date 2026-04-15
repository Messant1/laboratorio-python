from dataclasses import dataclass


class Persona:
    def __init__(self, nombre, edad, activo):
        self.nombre = nombre
        self.edad = edad
        self.activo = activo

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

    def es_mayor_de_edad(self):
        return self.edad >= 18


@dataclass
class PersonaData:
    nombre: str
    edad: int
    activo: bool

    def saludar(self):
        print(f"Hola, soy {self.nombre}")


class Empleado(Persona):
    def __init__(self, nombre, edad, activo, puesto):
        super().__init__(nombre, edad, activo)
        self.puesto = puesto

    def trabajar(self):
        print(f"{self.nombre} está trabajando como {self.puesto}")


if __name__ == "__main__":
    persona1 = Persona("Eric", 30, True)
    persona1.saludar()
    print("¿Es mayor de edad?", persona1.es_mayor_de_edad())

    empleado1 = Empleado("Eric", 30, True, "Data Analyst")
    empleado1.saludar()
    empleado1.trabajar()
    print("¿Es mayor de edad?", empleado1.es_mayor_de_edad())

    persona2 = PersonaData("Eric", 30, True)
    persona2.saludar()
    print(persona2)
