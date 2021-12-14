# distance_to_lightning_strike.py

def main():
    print("This program determines the distance to a lighteing strike,")
    print("using the time elapsed between seeing the flash and hearing thunder.")
    print()

    sec = eval(input("How many seconds elapsed between seeing flash and hearing thunder: "))

    dist_feet = 1100 * sec

    dist_miles = (1/5280) * dist_feet

    print(f"The distance to the lightning is {dist_miles} miles.")


main()
