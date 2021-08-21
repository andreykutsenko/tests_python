import math


class Circle:
    """Окружность - можно считать радиус, площадь, диаметр"""

    def __init__(self, radius):
        """Инициализация окружности. radius - радиус окружности"""
        self.radius = radius

    def get_area(self) -> float:
        """Вычисляет площадь круга"""
        return math.pi * self.radius**2

    def get_length(self) -> float:
        """Вычисляет длину окружности"""
        return 2 * math.pi * self.radius

    def get_diameter(self) -> float:
        """Возвращает диаметр окружности"""
        return 2 * self.radius

first_circle = Circle(radius=10)
second_circle = Circle(radius=20)

print(first_circle.get_area())
print(second_circle.get_diameter())