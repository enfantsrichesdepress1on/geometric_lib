```python
import math

def calculate_circle_area(radius):
    """
    Функция рассчитывает площадь круга по формуле S = π * R².
    :param radius: Радиус круга.
    :return: Площадь круга.
    """
    return math.pi * radius * radius

def calculate_rectangle_area(length, width):
    """
    Функция рассчитывает площадь прямоугольника по формуле S = a * b.
    :param length: Длина прямоугольника.
    :param width: Ширина прямоугольника.
    :return: Площадь прямоугольника.
    """
    return length * width

def calculate_square_area(side):
    """
    Функция рассчитывает площадь квадрата по формуле S = a².
    :param side: Длина стороны квадрата.
    :return: Площадь квадрата.
    """
    return side * side

def calculate_circle_perimeter(radius):
    """
    Функция рассчитывает периметр (длину окружности) по формуле P = 2πR.
    :param radius: Радиус круга.
    :return: Периметр круга.
    """
    return 2 * math.pi * radius

def calculate_rectangle_perimeter(length, width):
    """
    Функция рассчитывает периметр прямоугольника по формуле P = 2(a + b).
    :param length: Длина прямоугольника.
    :param width: Ширина прямоугольника.
    :return: Периметр прямоугольника.
    """
    return 2 * (length + width)

def calculate_square_perimeter(side):
    """
    Функция рассчитывает периметр квадрата по формуле P = 4a.
    :param side: Длина стороны квадрата.
    :return: Периметр квадрата.
    """
    return 4 * side

if __name__ == "__main__":
    # Примеры расчётов
    radius = 5.0
    print("Площадь круга:", calculate_circle_area(radius))
    print("Периметр круга:", calculate_circle_perimeter(radius))

    length = 10.0
    width = 4.0
    print("Площадь прямоугольника:", calculate_rectangle_area(length, width))
    print("Периметр прямоугольника:", calculate_rectangle_perimeter(length, width))

    side = 6.0
    print("Площадь квадрата:", calculate_square_area(side))
    print("Периметр квадрата:", calculate_square_perimeter(side))
```
