import pytest
from square import calculate_square_area, calculate_square_perimeter

def test_calculate_square_area_positive():
    side = 5.0
    expected = 25.0
    result = calculate_square_area(side)
    assert result == expected

def test_calculate_square_area_negative():
    side = -2.0
    with pytest.raises(ValueError):
        calculate_square_area(side)

def test_calculate_square_perimeter_positive():
    side = 5.0
    expected = 20.0
    result = calculate_square_perimeter(side)
    assert result == expected
