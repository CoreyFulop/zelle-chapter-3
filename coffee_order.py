# coffee_order.py

def main():
    print("This program determines the cost of an order from")
    print("the Konditorei coffee shop.")
    print()

    pounds = eval(input("How many pounds of coffee to order: "))

    price_per_pound = 0.86
    shipping_price = 1.50

    coffee_price = pounds * price_per_pound

    order_total = coffee_price + shipping_price

    print(f"The cost of an order is {order_total}.")


main()
