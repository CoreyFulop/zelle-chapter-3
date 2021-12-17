# pi_approximation.py

import math

def main():
    print("This program determines an approximation to pi,")
    print("by adding terms from a fancy sequence.")
    print("It then compares the approximation to math.pi.")
    n = eval(input("How many terms to add from the sequence: "))

    denominator = 1
    count = 0
    for  i in range(n):
        term = (-1)**i * (4/denominator)
        count += term
        denominator += 2

    print(f"Our approximation to pi is {count}.")
    print(f"math.pi - {count} = {math.pi-count}.")


main()
