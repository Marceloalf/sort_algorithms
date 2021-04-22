from quick_sort import quick


def test_ordenado(ordenada_crescente):
    esperado = sorted(ordenada_crescente)
    assert quick(ordenada_crescente) == esperado


def test_ordenada_decrescente(ordenada_decrescente):
    esperado = sorted(ordenada_decrescente)
    assert quick(ordenada_decrescente) == esperado


def test_aleatorio(aleatoria):
    esperado = sorted(aleatoria)
    assert quick(aleatoria) == esperado
