import pytest

from abs import abs


@pytest.mark.parametrize("a, expected", [
    (4, 4),
    (0, 0),
    (-3, 3),
])
def test_abs(a, expected):
    assert abs(a) == expected