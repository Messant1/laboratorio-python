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