# sum_n.py

def main():
    print("This program determines the sum of the first n natural numbers.")
    n = eval(input("Enter n: "))

    count = 0
    for i in range(1, n+1):
        count += i
    
    print()
    print(f"The sum of the first {n} natural numbers is {count}.")


main()
1