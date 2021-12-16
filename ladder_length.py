# ladder_length.py

import math

def main():
    print("This program determines the ladder length required")
    print("to reach a given height when leaned against a house.")
    print()

    height = eval(input("Enter the height of the point to reach: "))
    degrees = eval(input("Enter the angle (in degrees) the ladder makes with the house: "))

    radians = (math.pi/180) * degrees
    
    length = height/(math.sin(radians))

    print()
    print(f"We require a ladder of {length} length.")


main()
