import pytest
from rectangle import calculate_rectangle_area, calculate_rectangle_perimeter

def test_calculate_rectangle_area_positive():
    length = 4.0
    width = 2.0
    expected = 8.0
    result = calculate_rectangle_area(length, width)
    assert result == expected

def test_calculate_rectangle_area_negative():
    length = -4.0
    width = 2.0
    with pytest.raises(ValueError):
        calculate_rectangle_area(length, width)

def test_calculate_rectangle_perimeter_positive():
    length = 4.0
    width = 2.0
    expected = 2 * (length + width)
    result = calculate_rectangle_perimeter(length, width)
    assert result == expected
