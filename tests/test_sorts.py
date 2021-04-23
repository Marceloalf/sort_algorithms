import pytest

from bubble_sort import bubble
from heap_sort import heap
from insertion_sort import insertion
from merge_sort import merge
from quick_sort import quick
from selection_sort import selection_sort

CASOS_DE_TESTES = [
    [],
    [1],
    [0, 1, 2],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [12, 3, 5, 8, 10, 11, 4, 9, 2, 6, 1, 7, 12, 5, 10, 4, 1, 7, 8, 1, 1],
    [1, 1, 1, 1, 1],
    [i for i in range(10000, -1, -1)]
]


@pytest.mark.parametrize('caso', CASOS_DE_TESTES)
def test_bubble(caso):
    esperado = sorted(caso)
    assert bubble(caso) == esperado


@pytest.mark.parametrize('caso', CASOS_DE_TESTES)
def test_selection(caso):
    esperado = sorted(caso)
    assert selection_sort(caso) == esperado


@pytest.mark.parametrize('caso', CASOS_DE_TESTES)
def test_insertion(caso):
    esperado = sorted(caso)
    assert insertion(caso) == esperado


@pytest.mark.parametrize('caso', CASOS_DE_TESTES)
def test_heap(caso):
    esperado = sorted(caso)
    assert heap(caso) == esperado


@pytest.mark.parametrize('caso', CASOS_DE_TESTES)
def test_merge(caso):
    esperado = sorted(caso)
    assert merge(caso) == esperado


@pytest.mark.parametrize('caso', CASOS_DE_TESTES)
def test_quick(caso):
    esperado = sorted(caso)
    assert quick(caso) == esperado
