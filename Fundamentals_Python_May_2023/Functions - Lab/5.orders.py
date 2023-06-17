order = input()
count = int(input())
price = 0
def calculating_orders (order, count):
    if order == "coffee":
        price = count * 1.50
    elif order == "coke":
        price = count * 1.40
    elif order == "water":
        price = count * 1.00
    elif order == "snacks":
        price = count * 2.00

    return (f'{price :.2f}')

print(calculating_orders(order, count))