import pytest
from calculate import calc

def test_calc_circle_area_positive():
    args = ["circle", "area", "5"]
    result = calc(args)
    import math
    expected = math.pi * 25
    assert pytest.approx(result) == pytest.approx(expected)

def test_calc_circle_area_negative():
    args = ["circle", "area", "-5"]
    with pytest.raises(ValueError):
        calc(args)

def test_calc_invalid_arguments():
    args = ["circle", "unknown_op", "5"]
    with pytest.raises(ValueError):
        calc(args)
