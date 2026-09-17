import pytest

from sub import subtraction


@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 1),
    (0, 0, 0),
    (1, 1, 0),
])
def test_subtraction(a, b, expected):
    assert subtraction(a, b) == expected