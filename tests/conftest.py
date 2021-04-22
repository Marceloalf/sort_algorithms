from typing import List
import pytest


SESSION = 'session'


@pytest.fixture(scope=SESSION)
def ordenada_crescente() -> List[int]:
    return [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    ]


@pytest.fixture(scope=SESSION)
def ordenada_decrescente():
    return [
        12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
    ]


@pytest.fixture(scope=SESSION)
def aleatoria():
    return [
        12, 3, 5, 8, 10, 11, 4, 9, 2, 6, 1, 7
    ]
