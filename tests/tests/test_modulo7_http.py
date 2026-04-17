from laboratorio_python.modulo7_http import obtener_datos


def test_obtener_datos_ok():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = obtener_datos(url)

    assert isinstance(data, list)
    assert len(data) > 0
