import pytest

from abs import abs


@pytest.mark.parametrize("a, expected", [
    (3, 3),
    (0, 0),
    (-1, 1),
])
def test_abs(a, expected):
    assert abs(a) == expected