count_clients = int(input())
total_price = 0
price = 0
count_purchase = 0
total_purchase = 0
for i in range(count_clients):

    while True:
       product = input()
       if product == "Finish":
        break

       if product == "basket":
           price += 1.50

       elif product == "wreath":
           price += 3.80

       elif product == "chocolate bunny":
           price+= 7
       count_purchase += 1
       total_purchase += 1

    if count_purchase % 2 == 0:
        price -= price * 0.20
    total_price += price

    print(f"You purchased {count_purchase} items for {price :.2f} leva.")
    count_purchase = 0
    price = 0

average_price = total_price / count_clients
print(f"Average bill per client is: {average_price :.2f} leva.")