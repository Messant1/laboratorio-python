from dataclasses import dataclass

from pydantic import BaseModel, Field


# 🧠 Clase base (lógica)
class Usuario:
    def __init__(self, nombre, edad, activo):
        self.nombre = nombre
        self.edad = edad
        self.activo = activo

    def es_mayor_de_edad(self):
        return self.edad >= 18


# 🧱 Dataclass (estructura simple)
@dataclass
class UsuarioData:
    nombre: str
    edad: int
    activo: bool


# 🔥 Pydantic (validación tipo API)
class UsuarioInput(BaseModel):
    nombre: str = Field(min_length=1)
    edad: int = Field(ge=0, le=120)
    activo: bool


# 🔄 Conversión entre modelos
def convertir_a_usuario(data: UsuarioInput) -> Usuario:
    return Usuario(nombre=data.nombre, edad=data.edad, activo=data.activo)


# ▶ Ejecución
if __name__ == "__main__":
    # Simulando entrada tipo JSON
    entrada = {"nombre": "Eric", "edad": 30, "activo": True}

    # Validación con Pydantic
    usuario_validado = UsuarioInput(**entrada)

    print("Datos validados:", usuario_validado)

    # Conversión a objeto
    usuario = convertir_a_usuario(usuario_validado)

    print("¿Es mayor de edad?", usuario.es_mayor_de_edad())
