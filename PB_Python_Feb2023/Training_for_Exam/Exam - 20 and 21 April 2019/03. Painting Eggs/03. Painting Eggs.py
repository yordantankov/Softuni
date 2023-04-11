size_of_egg = input()
color_of_egg = input()
egg_quantity = int(input())
price = 0
if size_of_egg == "Large":
    if color_of_egg == "Red":
        price = 16
    elif color_of_egg == "Green":
        price = 12
    elif color_of_egg == "Yellow":
        price = 9

elif size_of_egg == "Medium":
    if color_of_egg == "Red":
        price = 13
    elif color_of_egg == "Green":
        price = 9
    elif color_of_egg == "Yellow":
        price = 7

elif size_of_egg == "Small":
    if color_of_egg == "Red":
        price = 9
    elif color_of_egg == "Green":
        price = 8
    elif color_of_egg == "Yellow":
        price = 5

total = egg_quantity * price
total -= total * 0.35

print(f'{total :.2f} leva.')
