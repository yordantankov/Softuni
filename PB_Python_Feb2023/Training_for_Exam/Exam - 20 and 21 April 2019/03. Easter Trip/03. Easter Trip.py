destination = input()
days = input()
nights = int(input())
price = 0
if destination == "France":
    if days == "21-23":
        price = 30
    elif days == "24-27":
        price = 35
    elif days == "28-31":
        price = 40

elif destination == "Italy":
    if days == "21-23":
        price = 28
    elif days == "24-27":
        price = 32
    elif days == "28-31":
        price = 39

elif destination == "Germany":
    if days == "21-23":
        price = 32
    elif days == "24-27":
        price = 37
    elif days == "28-31":
        price = 43


total = nights * price

print(f"Easter trip to {destination} : {total :.2f} leva.")
