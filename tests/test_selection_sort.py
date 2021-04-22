from selection_sort import selection_sort


def test_ordenado(ordenada_crescente):
    esperado = sorted(ordenada_crescente)
    assert selection_sort(ordenada_crescente) == esperado


def test_ordenada_decrescente(ordenada_decrescente):
    esperado = sorted(ordenada_decrescente)
    assert selection_sort(ordenada_decrescente) == esperado


def test_aleatorio(aleatoria):
    esperado = sorted(aleatoria)
    assert selection_sort(aleatoria) == esperado
