# sum_n_cubes.py

def main():
    print("This program determines the sum of cubes of the first n natural numbers.")
    n = eval(input("Enter n: "))

    count = 0
    for i in range(1, n+1):
        count += i**3

    print(f"The sum of the cubes of the first {n} natural numbers is {count}.")


main()
