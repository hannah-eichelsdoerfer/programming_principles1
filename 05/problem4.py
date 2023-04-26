# Problem: 
# Roll carpet comes in rolls 3.66 meters wide. 
# Carpet is charged by the total number of whole metres that need to be cut from the roll. 
# It may be laid in a rectangular room in a lengthways manner or widthways manner (see illustration below). 
# Either way there might be some wastage. 
# The length of a room is always its longer dimension and its width is always its shorter dimension.

# Write a program that repeatedly asks the user for room dimensions until either dimension entered is zero. 
# For each room print the length and width (to the nearest millimetre), and the total length of carpet required in whole metres, to cover the room in two scenarios: 
# - lengthways manner
# - widthways manner.
# Hints: make good use of standard library functions; and simplify your program by writing a function to compute the total carpet length required given the room dimensions. 

# Sample run:
# Enter room dimension 1 (m): 2.5
# Enter room dimension 2 (m): 5.5
# Length of room = 5.500 m
# Width of room = 2.500 m
# Total carpet length required in lengthways manner = 6 m
# Total carpet length required in widthways manner = 5 m
# Enter room dimension 1 (m): 7.4
# Enter room dimension 2 (m): 4.3
# Length of room = 7.400 m
# Width of room = 4.300 m
# Total carpet length required in lengthways manner = 15 m
# Total carpet length required in widthways manner = 13 m
# Enter room dimension 1 (m): 0
# Enter room dimension 2 (m): 0

import math

roll_width = 3.66

def total_carpet_length_required(length, width):
    lengthwise = math.ceil(width / roll_width) * length 
    widthwise = math.ceil(width / roll_width) * length

    return lengthwise, widthwise

while True:
    one = float(input("Enter room dimension 1 (m): "))
    two = float(input("Enter room dimension 2 (m): "))

    if one == 0 or two == 0:
        break

    length = max(one, two)
    width = min(one, two)

    print(f"Length of room = {length:.3f} m")
    print(f"Width of room = {width:.3f} m")

    lengthwise, widthwise = total_carpet_length_required(length, width)

    print(f"Total carpet length required in lengthways manner = {math.ceil(lengthwise)} m")
    print(f"Total carpet length required in widthwise manner = {math.ceil(widthwise)} m")



