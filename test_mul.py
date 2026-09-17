import pytest

from mul import multiplication


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 2),
    (0, 0, 0),
    (-1, 1, -1),
])
def test_multiplication(a, b, expected):
    assert multiplication(a, b) == expected