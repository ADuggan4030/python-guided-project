from base_polygon import BasePolygon
from abc import ABC


class BaseQuadrilateral(ABC, BasePolygon):

    def __init__(self, side_a, side_b, side_c, side_d):
        super().__init__(4)
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c
        self.__side_d = side_d

    @property
    def length(self) -> float:
        return self.__side_a

    @property
    def width(self) -> float:
        return self.__side_b

    @property
    def area(self) -> float:
        return self.length * self.width

    @property
    def height(self) -> float:
        return self.width

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.length)
