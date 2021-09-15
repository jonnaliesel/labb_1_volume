#cube volume s^3
#tetrahedron volume sqrt(2)*s^3 / 12

import math

figure = input("Hey, let's play with some Geometry!\nWanna get the volume of a cube or a tetrahedron?\nc/t : ")

while figure :
    if figure == 'c' :
        side = int(input('How many centimeters is each side of your cube? '))
        volume = side**3
        print('Cool! The volume of your cube with the side length of ' + str(side) + ' is equal to ' + str(volume) + ' cm3 or ' + str(volume/1000) + ' liters')
        figure = ''
    elif figure == 't' :
        side = int(input('How many centimeters is each side of your equilateral tetrahedron? '))
        volume = int(math.sqrt(2)*side**3/12)
        print('Cool! The volume of your tetrahedron with the side length of ' + str(side) + ' is equal to ' + str(volume) + ' cm3 or ' + str(volume/1000) + ' liters')
        figure = ''
    else :
        figure = input('Sorry, your input is not valid. Try again :)\nc/t : ')
    figure = input('Cool, wanna try again? :) Enter cube or tetrahedon c/t : ')
    