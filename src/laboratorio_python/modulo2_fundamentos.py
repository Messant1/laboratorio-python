import json


def cargar_datos(path):
    try:
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Archivo no encontrado")
        return []
    except json.JSONDecodeError:
        print("JSON inválido")
        return []


def filtrar_mayores(data):
    return [p for p in data if p["edad"] >= 18]


def contar_activos(data):
    return sum(1 for p in data if p["activo"])


data = cargar_datos("data.json")

mayores = filtrar_mayores(data)
activos = contar_activos(data)

print("Mayores de edad:", mayores)
print("Cantidad activos:", activos)
