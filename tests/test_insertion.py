from insertion_sort import insertion


def test_ordenado(ordenada_crescente):
    esperado = sorted(ordenada_crescente)
    assert insertion(ordenada_crescente) == esperado


def test_ordenada_decrescente(ordenada_decrescente):
    esperado = sorted(ordenada_decrescente)
    assert insertion(ordenada_decrescente) == esperado


def test_aleatorio(aleatoria):
    esperado = sorted(aleatoria)
    assert insertion(aleatoria) == esperado
