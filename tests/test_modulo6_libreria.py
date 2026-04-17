from laboratorio_python.modulo6_libreria import procesar_datos


def test_procesar_datos_ok():
    rows = [
        {"cliente": "A", "monto": "100"},
        {"cliente": "A", "monto": "50"},
        {"cliente": "B", "monto": "200"},
    ]

    resultado = procesar_datos(rows)

    assert resultado["A"] == 150
    assert resultado["B"] == 200


def test_procesar_datos_valor_invalido():
    rows = [
        {"cliente": "A", "monto": "100"},
        {"cliente": "A", "monto": "abc"},
    ]

    resultado = procesar_datos(rows)

    assert resultado["A"] == 100
