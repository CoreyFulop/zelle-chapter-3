# fibonacci.py

def main():
    print("This program computes the nth Fibonacci number.")
    n  = eval(input("Enter n: "))

    first = 0
    second = 1

    for i in range(1, n):
        first, second = second, first + second

    print(f"The {n} Fibonacci number is {second}")


main()
