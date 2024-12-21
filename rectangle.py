def area(length, width):
    """
    Вычисляет площадь прямоугольника.

    Параметры:
    length, width (int): Длина и ширина прямоугольника.

    Возвращает:
    int: Площадь прямоугольника.

    Пример вызова:
    area(10, 4)  # Возвращает 40
    """
    return length * width

def perimeter(length, width):
    """
    Вычисляет периметр прямоугольника.

    Параметры:
    length, width (int): Длина и ширина прямоугольника.

    Возвращает:
    int: Периметр прямоугольника.

    Пример вызова:
    perimeter(10, 4)  # Возвращает 28
    """
    return 2 * (length + width)

if __name__ == "__main__":
    length = 10
    width = 4
    print("Площадь прямоугольника:", area(length, width))
    print("Периметр прямоугольника:", perimeter(length, width))
