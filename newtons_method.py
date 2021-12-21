# newtons_method.py
# Approximates the square root of a value, using Newton's method.

import math

def main():
    print("This program finds an approximation to a square root of an input value,")    
    print("using Newton's method.")
    print()

    x = eval(input("Enter a number to find the (approximate) square root of: "))
    n = eval(input("How many times to apply the loop of Newton's method: "))

    guess = x/2
    for i in range(n):
        guess = (guess + (x/guess))/2

    print()
    print(f"The approximation is {guess}.")
    print(f"Now math.sqrt({x}) - our approximation is {math.sqrt(x) - guess}.")


main()
