# find_average.py

def main():
    print("This program determines the mean average of n numbers.")
    n = eval(input("How many numbers to find the average of: "))

    count = 0
    for i in range(n):
        number = eval(input("Enter a number: "))
        count += number

    average = count/n

    print(f"The average of the {n} numbers is {average}.")


main()
