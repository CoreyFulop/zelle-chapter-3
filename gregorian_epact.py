# gregorian_epact.py

def main():
    print("This program determines the Gregorian epact for a given year.")
    year = eval(input("Please enter the year: "))

    C = year//100

    epact = (8 + (C//4) - C + ((8*C + 13)//25) + 11 * (year%19))%30

    print()
    print(f"The Gregorian epact for {year} is {epact}.")


main()
