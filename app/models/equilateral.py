from app.models import base_triangle
from math import pow
from math import sqrt


class Equilateral(base_triangle.BaseTriangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length, side_length)

    @property
    def height(self) -> float:
        return sqrt(pow(self.side_a, 2) - pow(self.side_b / 2, 2))