import pytest

from div import division


@pytest.mark.parametrize("a, b, expected", [
    (4, 2, 2.0),
    (9, 3, 3.0),
    (5, 2, 2.5),
])
def test_division(a, b, expected):
    assert division(a, b) == expected

def test_division_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        division(1, 0)