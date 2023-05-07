budjet = float(input())
total_count = 0
count = 0
sum = 0
while True:
    product = input()
    if product == "Stop":
        break
    price_product = float(input())
    count += 1
    if count == 3:
        price_product /= 2
        count = 0

    if price_product > budjet:
        print("You don't have enough money!")
        diff = price_product - budjet
        print(f'You need {diff :.2f} leva!')
        exit()

    budjet -= price_product
    total_count += 1
    sum += price_product

print(f"You bought {total_count} products for {sum :.2f} leva.")