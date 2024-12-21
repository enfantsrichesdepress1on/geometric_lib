import pytest
from square import area, perimeter

def test_calculate_square_area_positive():
    side = 5.0
    expected = 25.0
    result = area(side)
    assert result == expected

def test_calculate_square_area_negative():
    side = -2.0
    with pytest.raises(ValueError):
        area(side)

def test_calculate_square_perimeter_positive():
    side = 5.0
    expected = 20.0
    result = perimeter(side)
    assert result == expected
