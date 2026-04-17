import csv
import json
import logging
from collections import defaultdict
from pathlib import Path

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def leer_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        logging.error(f"El archivo no existe: {path}")
        raise FileNotFoundError(f"No se encontró el archivo: {path}")

    with path.open(mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def procesar_datos(rows: list[dict[str, str]]) -> dict[str, float]:
    totales = defaultdict(float)

    for row in rows:
        try:
            cliente = row["cliente"]
            monto = float(row["monto"])
            totales[cliente] += monto
        except KeyError as e:
            logging.warning(f"Columna faltante: {e}")
        except ValueError:
            logging.warning(f"Valor inválido en fila: {row}")

    return dict(totales)


def guardar_json(data: dict[str, float], output_path: Path) -> None:
    # 🔥 mejora pro: asegura que exista la carpeta
    output_path.parent.mkdir(parents=True, exist_ok=True)

    output_path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def run_pipeline(input_path: Path, output_path: Path) -> None:
    rows = leer_csv(input_path)
    resultado = procesar_datos(rows)
    guardar_json(resultado, output_path)


def main() -> None:
    input_path = Path("data/sales.csv")
    output_path = Path("data/resultado.json")

    logging.info("Iniciando proceso")

    try:
        # ✅ AQUÍ está el cambio importante
        run_pipeline(input_path, output_path)

        logging.info("Proceso completado correctamente")

    except Exception:
        logging.exception("Error en ejecución")


if __name__ == "__main__":
    main()
