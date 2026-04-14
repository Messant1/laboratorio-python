import random
import time


def saludar(nombre):
    print("Hola", nombre)


def sumar(a, b):
    return a + b


def generar_lotes(lista, tamaño):
    for i in range(0, len(lista), tamaño):
        yield lista[i : i + tamaño]


def reintentos(max_intentos=3):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for intento in range(max_intentos):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}, reintentando {intento+1}/{max_intentos}")
                    time.sleep(1)
            print("Falló después de varios intentos")

        return wrapper

    return decorador


# FUNCION DECORADA
@reintentos(max_intentos=3)
def funcion_inestable():
    if random.random() < 0.7:
        raise ValueError("Fallo aleatorio")
    return "Funcionó!"


# EJECUCION CONTROLADA
if __name__ == "__main__":
    saludar("Axity")

    resultado = sumar(2, 3)
    print(resultado)

    datos = [1, 2, 3, 4, 5, 6, 7]
    for lote in generar_lotes(datos, 3):
        print(lote)

    print(funcion_inestable())
