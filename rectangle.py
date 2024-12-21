def area(a, b):
    """
    Вычисляет площадь прямоугольника.

    Параметры:
    a, b (int): Длина и ширина прямоугольника.

    Возвращает:
    int: Площадь прямоугольника.

    Пример вызова:
    area(10, 4)  # Возвращает 40
    """
    return a * b

def perimeter(a, b):
    """
    Вычисляет периметр прямоугольника.

    Параметры:
    a, b (int): Длина и ширина прямоугольника.

    Возвращает:
    int: Периметр прямоугольника.

    Пример вызова:
    perimeter(10, 4)  # Возвращает 14
    """
    return a + b

if __name__ == "__main__":
    a = 10
    b = 4
    print("Площадь прямоугольника:", area(a, b))
    print("Периметр прямоугольника:", perimeter(a, b))
