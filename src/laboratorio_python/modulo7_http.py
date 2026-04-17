import json
import logging
import time
from pathlib import Path

import httpx

logging.basicConfig(level=logging.INFO)


def obtener_datos(url: str) -> dict:
    try:
        response = httpx.get(url, timeout=5.0)
        response.raise_for_status()
        return response.json()

    except httpx.TimeoutException:
        logging.error("Timeout al hacer request")

    except httpx.HTTPStatusError as e:
        logging.error(f"Error HTTP: {e.response.status_code}")

    except Exception:
        logging.exception("Error inesperado")

    return {}


def obtener_datos_con_reintento(url: str, retries: int = 3) -> dict:
    for intento in range(retries):
        resultado = obtener_datos(url)

        if resultado:
            return resultado

        logging.warning(f"Reintento {intento + 1}")
        time.sleep(1)

    return {}


def guardar_respuesta(data: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def run_pipeline(url: str, output_path: Path) -> None:
    data = obtener_datos_con_reintento(url)
    guardar_respuesta(data, output_path)


def main() -> None:
    url = "https://jsonplaceholder.typicode.com/posts"
    output_path = Path("data/posts.json")

    logging.info("Iniciando descarga")

    run_pipeline(url, output_path)

    logging.info("Descarga completada")


if __name__ == "__main__":
    main()
