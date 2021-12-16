# sum_n_values.py

def main():
    print("This program sums n numbers specified by the user.")
    n = eval(input("How many numbers to sum: "))

    count = 0
    for i in range(n):
        number = eval(input("Enter a number to add: "))
        count += number

    print(f"The sum of the {n} numbers is {count}.")


main()
