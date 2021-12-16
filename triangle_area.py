# triangle_area.py

import math

def main():
    print("This program determines the area of a tringle")
    print("with sides a, b, and c.")
    print()

    a = eval(input("Enter the length of side a: "))
    b = eval(input("Enter the length of side b: "))
    c = eval(input("Enter the length of side c: "))

    s = (a + b + c)/2

    A = math.sqrt(s*(s-a)*(s-b)*(s-c))

    print()
    print(f"The triangle has area {A}.")


main()
