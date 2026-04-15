# laboratorio-python
Repositorio para seguimiento al curso Pyhton - Axity y sus laboratorios
## Módulo 1 - Entorno y herramientas

En este laboratorio se configuró el entorno de desarrollo para Python.

### Actividades realizadas
- Instalación de Python 3.14
- Configuración de entorno virtual con Poetry
- Configuración de Visual Studio Code como IDE
- Uso de formateadores y linters:
  - black (formato de código)
  - isort (orden de imports)
  - ruff (análisis estático)
- Configuración de pre-commit para validación automática antes de commits

### Comandos utilizados
```bash
poetry install
poetry add --group dev black isort ruff pre-commit
pre-commit install

## Módulo 2 - Fundamentos
Script que:
- Lee archivo JSON
- Filtra mayores de edad
- Cuenta registros activos
- Maneja errores de archivo y formato

## Módulo 3 - Programación Pythonic
- Uso de funciones con parámetros y retorno
- Generadores con yield para procesamiento por lotes
- Implementación de decorador para reintentos con manejo de errores

## Módulo 4 - Validación con Pydantic
Pydantic install
El modelo valida los datos de entrada.  
Ejemplo de error:
Si edad = -5 → lanza error de validación.