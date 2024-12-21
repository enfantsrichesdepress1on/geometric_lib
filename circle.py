import math

def area(radius):
    """
    Вычисляет площадь круга.

    Параметры:
    radius (int): Радиус круга.

    Возвращает:
    float: Площадь круга.

    Пример вызова:
    area(5)  # Возвращает 78.53981633974483
    """
    return math.pi * radius * radius

def perimeter(radius):
    """
    Вычисляет длину окружности.

    Параметры:
    radius (int): Радиус круга.

    Возвращает:
    float: Периметр круга.

    Пример вызова:
    perimeter(5)  # Возвращает 31.41592653589793
    """
    return 2 * math.pi * radius
