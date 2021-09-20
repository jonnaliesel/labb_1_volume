'''
A program that calculates the volume of different geometrical figures
'''

import math

def volume_of_cube(side_length):
    return side_length**3

def volume_of_tetrahedron(side_length):
    return math.sqrt(2)*side_length**3/12

figure = input(
    "Hey, let's play with some Geometry!\n\
    Wanna get the volume of a cube or a tetrahedron?\n\
    c/t : "
)

while figure is not None :
    if (figure == 'c') :
        side_length = eval(input(
            '\nHow many centimeters is each side of your cube? '
        ))

        volume = volume_of_cube(side_length)
        liters = volume/1000
        print(
            f'\nCool! The volume of your cube with the side length of \
            {side_length} is equal to {volume} cm3 or {liters} liters'
        )
    elif figure == 't' :
        side_length = eval(input(
            '\nHow many centimeters is each side of your equilateral tetrahedron? '
        ))
        volume = volume_of_tetrahedron(side_length)
        liters = volume/1000

        print(
            f'\nCool! The volume of your tetrahedron with the side length of \
            {side_length} is equal to {volume} cm3 or {liters} liters'
        )
    else :
        figure = input(
            '\nSorry, your input is not valid. Try again :)\n\c/t : '
        )
    
    figure = input('Wanna try again? :) Enter cube or tetrahedon c/t : ')