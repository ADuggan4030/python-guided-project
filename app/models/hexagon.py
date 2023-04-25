from app.models import base_polygon
from math import pow
from math import sqrt


class Hexagon(base_polygon.BasePolygon):

    def __init__(self, side_a, side_b, side_c, side_d, side_e, side_f):
        super().__init__(6)
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c
        self.__side_d = side_d
        self.__side_e = side_e
        self.__side_f = side_f

    @property
    def area(self) -> float:
        return 3 * sqrt(3) / 2 * pow(self.__side_a, 2)

    @property
    def height(self) -> float:
        return self.__side_a * 1.732

    @property
    def perimeter(self) -> float:
        return self.__side_a * self.sides

