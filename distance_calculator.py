# distance_calculator.py

import math

def main():
    print("This program determines the distance")
    print("between two points in the x-y plane.")
    print()

    x1, y1 = eval(input("Enter the x and y coordinate of the first point, separated by a comma: "))
    x2, y2 = eval(input("Enter the x and y coordinate of the second point, separated by a comma: "))

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    print()
    print(f"The distance between the two points is {distance}.")


main()
