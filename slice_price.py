# slice_price.py
# Determines the cost per square inch of a pizza

import math

def main():
    print("This program determines the price per square inch of a pizza.")
    print()

    diameter = eval(input("What is the diameter of the pizza: "))
    price = eval(input("What is the price of the pizza: "))

    radius = diameter / 2

    area = math.pi * radius**2

    price_per_area = area / price

    print()
    print(f"The cost per square inch of this pizza is {price_per_area}.")


main()
