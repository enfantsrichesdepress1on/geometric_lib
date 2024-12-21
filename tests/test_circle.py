import pytest
from circle import calculate_circle_area, calculate_circle_perimeter
import math

def test_calculate_circle_area_positive():
    radius = 5.0
    expected = math.pi * radius * radius
    result = calculate_circle_area(radius)
    assert pytest.approx(result) == pytest.approx(expected)

def test_calculate_circle_area_zero():
    radius = 0.0
    expected = 0.0
    result = calculate_circle_area(radius)
    assert result == expected

def test_calculate_circle_area_negative():
    radius = -3.0
    with pytest.raises(ValueError):
        calculate_circle_area(radius)

def test_calculate_circle_perimeter_positive():
    radius = 5.0
    expected = 2 * math.pi * radius
    result = calculate_circle_perimeter(radius)
    assert pytest.approx(result) == pytest.approx(expected)
