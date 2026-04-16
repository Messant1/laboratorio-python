from typing import Dict, List, Optional, TypedDict, Union


class UsuarioDict(TypedDict):
    nombre: str
    edad: int


def sumar(a: int, b: int) -> int:
    return a + b


def filtrar_mayores(edades: List[int]) -> List[int]:
    return [e for e in edades if e >= 18]


def procesar_usuario(usuario: Dict[str, str]) -> str:
    return f"Usuario: {usuario['nombre']}"


def obtener_nombre(nombre: Optional[str]) -> str:
    if nombre is None:
        return "Sin nombre"
    return nombre


def duplicar(valor: Union[int, str]) -> Union[int, str]:
    return valor * 2


if __name__ == "__main__":
    print(sumar(2, 3))

    edades = [10, 20, 30, 15]
    print(filtrar_mayores(edades))

    usuario = {"nombre": "Eric"}
    print(procesar_usuario(usuario))

    print(obtener_nombre(None))
    print(duplicar(5))
    print(duplicar("Hi"))

    usuario_tipado: UsuarioDict = {"nombre": "Eric", "edad": 30}
    print(usuario_tipado)
