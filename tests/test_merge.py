from merge_sort import merge


def test_ordenado(ordenada_crescente):
    esperado = sorted(ordenada_crescente)
    assert merge(ordenada_crescente) == esperado


def test_ordenada_decrescente(ordenada_decrescente):
    esperado = sorted(ordenada_decrescente)
    assert merge(ordenada_decrescente) == esperado


def test_aleatorio(aleatoria):
    esperado = sorted(aleatoria)
    assert merge(aleatoria) == esperado
