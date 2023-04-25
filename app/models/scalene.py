from app.models import base_triangle
from math import sqrt


class Scalene(base_triangle.BaseTriangle):

    def __init__(self, side_a, side_b, side_c):
        super().__init__(side_a, side_b, side_c)

    @property
    def semi_perimeter(self) -> float:
        return self.perimeter / 2

    @property
    def area(self) -> float:
        # sqrt ( s(s-a) * (s-b) * (s-c) )
        return sqrt(self.semi_perimeter * (self.semi_perimeter - self.side_a) *
                    (self.semi_perimeter - self.side_b) * (self.semi_perimeter - self.side_c))

    @property
    def height(self) -> float:
        value1: float = self.side_a + self.side_b + self.side_c
        value2: float = -self.side_a + self.side_b + self.side_c
        value3: float = self.side_a - self.side_b + self.side_c
        value4: float = self.side_a + self.side_b - self.side_c
        return .5 * sqrt(value1 * value2 * value3 * value4) / self.side_b




