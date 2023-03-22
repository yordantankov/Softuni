fruit = input()
size = input()
count_bought = int(input())
price = 0
if fruit == "Watermelon":
    if size == "small":
        price = count_bought * (2 * 56.00)
    elif size == "big":
        price = count_bought * (5 * 28.70)

elif fruit == "Mango":
    if size == "small":
        price = count_bought * (2 * 36.66)
    elif size == "big":
        price = count_bought * (5 * 19.60)

elif fruit == "Pineapple":
    if size == "small":
        price = count_bought * (2 * 42.10)
    elif size == "big":
        price = count_bought * (5 * 24.80)

elif fruit == "Raspberry":
    if size == "small":
        price = count_bought * (2 * 20.00)
    elif size == "big":
        price = count_bought * (5 * 15.20)

if price >= 400 and price <= 1000:
    price -= price * 0.15
elif price > 1000:
    price /= 2

print(f'{price :.2f} lv.')