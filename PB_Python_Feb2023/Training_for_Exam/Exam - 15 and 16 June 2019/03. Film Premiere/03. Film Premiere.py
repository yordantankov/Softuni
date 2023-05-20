film_name = input()
package = input()
tickets_qty = int(input())

price = 0

if film_name == "John Wick":
    if package == "Drink":
        price = 12
    elif package == "Popcorn":
        price = 15
    elif package == "Menu":
        price = 19

elif film_name == "Star Wars":
    if package == "Drink":
        price = 18
    elif package == "Popcorn":
        price = 25
    elif package == "Menu":
        price = 30

elif film_name == "Jumanji":
    if package == "Drink":
        price = 9
    elif package == "Popcorn":
        price = 11
    elif package == "Menu":
        price = 14

total = price * tickets_qty

if film_name == "Star Wars" and tickets_qty >= 4:
    total -= total * 0.30

if film_name == "Jumanji" and tickets_qty == 2:
    total -= total * 0.15

print(f'Your bill is {total :.2f} leva.')
