from heap_sort import heap


def test_ordenado(ordenada_crescente):
    esperado = sorted(ordenada_crescente)
    assert heap(ordenada_crescente) == esperado


def test_ordenada_decrescente(ordenada_decrescente):
    esperado = sorted(ordenada_decrescente)
    assert heap(ordenada_decrescente) == esperado


def test_aleatorio(aleatoria):
    esperado = sorted(aleatoria)
    assert heap(aleatoria) == esperado
