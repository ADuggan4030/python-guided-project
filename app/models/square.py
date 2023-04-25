from app.models import base_quadrilateral


class Square(base_quadrilateral.BaseQuadrilateral):
    def __init__(self, side_length):
        super().__init__(side_length, side_length, side_length, side_length)