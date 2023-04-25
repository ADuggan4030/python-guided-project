from app.models.square import Square
from app.models.rectangle import Rectangle
from app.models.parallelogram import Parallelogram
from app.models.pentagon import Pentagon
from app.models.hexagon import Hexagon
from app.models.isosceles import Isosceles
from app.models.equilateral import Equilateral
from app.models.scalene import Scalene


def precision_value(value: float) -> float:
    return round(value, 3)


def process_square(sq: Square):
    print(f'The height of this square is {precision_value(sq.height)}')
    print(f'The perimeter of this square is {precision_value(sq.perimeter)}')
    print(f'The area of this square is {precision_value(sq.area)}')


def process_rectangle(rect: Rectangle):
    print(f'The height of this rectangle is {precision_value(rect.height)}')
    print(f'The perimeter of this rectangle is {precision_value(rect.perimeter)}')
    print(f'The area of this rectangle is {precision_value(rect.area)}')


def process_parallelogram(parallel: Parallelogram):
    print(f' The height of this parallelogram is {precision_value(parallel.height)}')
    print(f' The perimeter of this parallelogram is {precision_value(parallel.perimeter)}')
    print(f' The area of this parallelogram is {precision_value(parallel.area)}')


def process_pentagon(pent: Pentagon):
    print(f' The height of this pentagon is {precision_value(pent.height)}')
    print(f' The perimeter of this pentagon is {precision_value(pent.perimeter)}')
    print(f' The area of this pentagon is {precision_value(pent.area)}')


def process_hexagon(hexagon: Hexagon):
    print(f' The height of this hexagon is {precision_value(hexagon.height)}')
    print(f' The perimeter of this hexagon is {precision_value(hexagon.perimeter)}')
    print(f' The area of this hexagon is {precision_value(hexagon.area)}')


def process_isosceles(iso: Isosceles):
    print(f' The height of this isosceles triangle is {precision_value(iso.height)}')
    print(f' The perimeter of this isosceles triangle is {precision_value(iso.perimeter)}')
    print(f' The area of this isosceles triangle is {precision_value(iso.area)}')


def process_equilateral(equ: Equilateral):
    print(f' The height of this equilateral triangle is {precision_value(equ.height)}')
    print(f' The perimeter of this equilateral triangle is {precision_value(equ.perimeter)}')
    print(f' The area of this equilateral triangle is {precision_value(equ.area)}')


def process_scalene(sca: Scalene):
    print(f' The height of this scalene triangle is {precision_value(sca.height)}')
    print(f' The perimeter of this scalene triangle is {precision_value(sca.perimeter)}')
    print(f' The area of this scalene triangle is {precision_value(sca.area)}')
