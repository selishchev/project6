# Calculation areas of figures

import math


def circle(r):
    """Calculating the area of a circle"""
    return math.pi * r ** 2


def triangle(x, h):
    """Calculating the area of a triangle"""
    return 0.5 * x * h


def rectangle(a, b):
    """Calculating the area of a rectangle"""
    return a * b


def right_polygon_of_n_sides(y, n):
    """Calculating the area of a right polygon of n sides"""
    return (n * y ** 2) / 4 * (math.tan(math.pi / n) ** (-1))


def main():
    try:
        number = None
        while number != 1 or number != 2 or number != 3 or number != 4:
            number = int(input('Enter the number of your figure'
                               '(1-circle, 2-triangle, 3-rectangle, 4-right polygon of n sides): '))
            if number == 1:
                r1 = float(input('Enter the radius of your circle: '))
                print('The area of your circle: ', circle(r1))
            elif number == 2:
                x1 = float(input('Enter the base of your triangle: '))
                h1 = float(input('Enter the height of your triangle: '))
                print('The area of your triangle: ', triangle(x1, h1))
            elif number == 3:
                a1 = float(input('Enter the length of the first side of your rectangle: '))
                b1 = float(input('Enter the length of the second side of your rectangle: '))
                print('The area of your rectangle: ', rectangle(a1, b1))
            elif number == 4:
                y1 = float(input('Enter the length of the side of your polygon: '))
                n1 = float(input('Enter the amount of sides in your polygon: '))
                print('The area of your polygon: ', right_polygon_of_n_sides(y1, n1))
    except ValueError:
        print('Looks like you entered the wrong value! Please, rerun the program and enter the right values.')


if __name__ == '__main__':
    main()
