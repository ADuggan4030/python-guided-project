from abc import ABC
from abc import abstractmethod


class BasePolygon(ABC):

    def __init__(self, sides: int):
        self.__sides = sides

    @property
    def sides(self) -> int:
        return self.__sides

    @property
    @abstractmethod
    def area(self) -> float:
        pass

    @property
    @abstractmethod
    def height(self) -> float:
        pass

    @property
    @abstractmethod
    def perimeter(self) -> float:
        pass

    