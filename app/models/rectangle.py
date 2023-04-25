from app.models import base_quadrilateral


class Rectangle(base_quadrilateral.BaseQuadrilateral):
    def __init__(self, side_length, side_width):
        super().__init__(side_length, side_width, side_length, side_width)
