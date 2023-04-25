from app.models import base_polygon
from math import sqrt
from math import pow


class Pentagon(base_polygon.BasePolygon):

    def __init__(self, side_a, side_b, side_c, side_d, side_e):
        super().__init__(5)
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c
        self.__side_d = side_d
        self.__side_e = side_e

    @property
    def area(self) -> float:
        value: float = 5 * (5 + 2 * sqrt(5))
        return .25 * sqrt(value) * pow(self.__side_a, 2)

    @property
    def height(self) -> float:
        return self.__side_a * sqrt(5 + 2 * sqrt(5)) / 2

    @property
    def perimeter(self) -> float:
        return self.__side_a * 5
