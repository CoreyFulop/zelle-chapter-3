# sphere_stats.py
# Determines the volume and area of a sphere,
# given radius as an input.

import math

def main():
    print("This program determines the volume and surface area of a sphere.")
    print()

    radius = eval(input("Please enter the radius: "))

    volume = (4/3) * math.pi * radius**2

    area = 4 * math.pi * radius**2

    print()
    print(f"The volume is {volume} and the surface area is {area}.")


main()
