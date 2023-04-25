import controller.controller as control

""" Beginning of the application """


def test_polygon():
    my_polygon = control.Scalene(42, 65, 50)
    control.process_scalene(my_polygon)


def welcome():
    print('Welcome to Widget Wonders.')
    print('What shape would you like to calculate today?')
    shape = input('1 for quadrilaterals & 2 for Triangles, 3 for Hexagon, or 4 for Pentagon')
    validate_shape(shape)


def validate_shape(shape: str):
    if shape == '1':
        quad_choices()
    elif shape == '2':
        triangle_choices()
    elif shape == '3':
        choice_hexagon()
    elif shape == '4':
        choice_pentagon()
    else:
        print('You provided an invalid option. Please try again.')


def quad_choices():
    print('Please choose from the following shapes.')
    item = input('1 for square, 2 for rectangle, 3 for parallelogram.')
    validate_quad(item)


def triangle_choices():
    print('Please choose from the following choices.')
    item = input('1 for equilateral, 2 for isosceles, 3 for scalene.')
    validate_triangle(item)


def validate_quad(choice: str):
    if choice == '1':
        choice_square()
    elif choice == '2':
        choice_rectangle()
    elif choice == '3':
        choice_parallelogram()
    else:
        print('You provided an invalid option. Please try again.')


def validate_triangle(choice: str):
    if choice == '1':
        choice_equilateral()
    elif choice == '2':
        choice_isosceles()
    elif choice == '3':
        choice_scalene()
    else:
        print('You provided an invalid option. Please try again.')


def choice_square():
    print('Thank you for choosing the square.')
    side = float(input('What are the numerical digits length of any side?'))
    my_square = control.Square(side)
    control.process_square(my_square)


def choice_rectangle():
    print('Thank you for choosing the rectangle.')
    length = float(input('What are the numerical digits for length?'))
    width = float(input('What are the numerical digits for width?'))
    my_rectangle = control.Rectangle(length, width)
    control.process_rectangle(my_rectangle)


def choice_parallelogram():
    print('Thank you for choosing the parallelogram.')
    length = float(input('What are the numerical digits for length?'))
    width = float(input('What are the numerical digits for width?'))
    my_parallelogram = control.Parallelogram(length, width)
    control.process_parallelogram(my_parallelogram)


def choice_hexagon():
    print('Thank you for choosing the hexagon.')
    side = float(input('What is the length in numerical digits of this regular hexagon?'))
    my_hexagon = control.Hexagon(side, side, side, side, side, side)
    control.process_hexagon(my_hexagon)


def choice_pentagon():
    print('Thank you for choosing the pentagon.')
    side = float(input('What is the side length in numerical digits of this regular pentagon?'))
    my_pentagon = control.Pentagon(side, side, side, side, side)
    control.process_pentagon(my_pentagon)


def choice_equilateral():
    print('Thank you for choosing the equilateral triangle.')
    side = float(input('What is the side length in numerical digits of this e. triangle?'))
    my_equilateral = control.Equilateral(side)
    control.process_equilateral(my_equilateral)


def choice_isosceles():
    print('Thank you for choosing the isosceles triangle.')
    side_a = float(input('What are the lengths in numerical digits for the two longest sides?'))
    side_b = float(input('What is the length in numerical digits for the short side?'))
    my_isosceles = control.Isosceles(side_a, side_b)
    control.process_isosceles(my_isosceles)


def choice_scalene():
    print('Thank you for choosing the scalene triangle.')
    side_a = float(input('What is the length in numerical digits for side_a?'))
    side_b = float(input('What is the length in numerical digits for side_b?'))
    side_c = float(input('What is the length in numerical digits for side_c?'))
    my_scalene = control.Scalene(side_a, side_b, side_c)
    control.process_scalene(my_scalene)


def main():
    welcome()


if __name__ == '__main__':
    main()
