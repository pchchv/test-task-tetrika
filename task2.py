def task(x1, y1, x2, y2, x3, y3, x4, y4):
    """В функцию передаются координаты двух противоположных вершин одного прямоугольника и
    двух противоположных вершин второго прямоугольника.
    1. Пересекаются ли эти прямоугольники?
    2. Найти площадь пересечения
    """
    result = intersection(x1, y1, x2, y2, x3, y3, x4, y4)
    if result == 0:
        return 'Прямоугольники не пересекаются'
    return 'Площадь пересечения прямоугольников: ' + str(result)


def intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    left = max(x1, x3)
    top = min(y2, y4)
    right = min(x2, x4)
    bottom = max(y1, y3)
    width = right - left  # ширина пересечения
    height = top - bottom  # высота пересечения
    if width < 0 or height < 0:
        return 0
    return width * height


print(task(1, 1, 2, 2, 3, 3, 4, 4))  # не пересекаются
print(task(1, 1, 2, 3, 1, 1, 3, 2))  # площадь пересечения: 1
print(task(0, 1, 4, 3, 2, 2, 4, 4))  # площадь пересечения: 2
print(task(0, 0, 2, 3, 0, 0, 2, 3))  # площадь пересечения: 6
