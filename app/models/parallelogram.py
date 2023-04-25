from app.models import base_quadrilateral
from math import sin
from math import radians


class Parallelogram(base_quadrilateral.BaseQuadrilateral):

    def __init__(self, side_length, side_width):
        super().__init__(side_length, side_width, side_length, side_width)

    @property
    def area(self) -> float:
        return self.length * self.width * sin(radians(45))

    @property
    def height(self) -> float:
        return self.area / self.length
