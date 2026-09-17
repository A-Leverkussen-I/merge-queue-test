import pytest

from add import add


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_addition(a, b, expected):
    assert add(a, b) == expected