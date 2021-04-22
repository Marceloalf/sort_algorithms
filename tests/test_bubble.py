from bubble_sort import bubble


def test_ordenado(ordenada_crescente):
    esperado = sorted(ordenada_crescente)
    assert bubble(ordenada_crescente) == esperado


def test_ordenada_decrescente(ordenada_decrescente):
    esperado = sorted(ordenada_decrescente)
    assert bubble(ordenada_decrescente) == esperado


def test_aleatorio(aleatoria):
    esperado = sorted(aleatoria)
    assert bubble(aleatoria) == esperado
