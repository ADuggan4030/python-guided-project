from base_polygon import BasePolygon
from abc import ABC


class BaseTriangle(BasePolygon, ABC):

    def __init__(self, side_a, side_b, side_c):
        super().__init__(3)
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    @property
    def side_a(self) -> float:
        return self.__side_a

    @property
    def side_b(self) -> float:
        return self.__side_b

    @property
    def side_c(self) -> float:
        return self.__side_c

    @property
    def area(self) -> float:
        return .5 * self.__side_a * self.height

    @property
    def perimeter(self) -> float:
        return self.__side_a + self.__side_b + self.__side_c

