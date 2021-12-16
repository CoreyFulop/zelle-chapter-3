# slope_calculator.py

def main():
    print("This program determines the slope of a line")
    print("joining two points in the x-y plane.")
    print()

    x1, y1 = eval(input("Enter the x and y coordinate of the first point, separated by a comma: "))
    x2, y2 = eval(input("Enter the x and y coordinate of the second point, separated by a comma: "))

    slope = (y2 - y1)/(x2 - x1)

    print()
    print(f"The slope joining the two points is {slope}.")


main()
