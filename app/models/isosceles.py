from app.models import base_triangle
from math import pow
from math import sqrt


class Isosceles(base_triangle.BaseTriangle):

    def __init__(self, side_a, side_b):
        super().__init__(side_a, side_b, side_a)

    @property
    def height(self) -> float:
        return sqrt(pow(self.side_a, 2) - (pow(self.side_b, 2) / 4))

