import math

guest_count = int(input())
budjet = float(input())

easter_bread_needed = math.ceil(guest_count / 3)
price_for_breads = easter_bread_needed * 4.00
eggs_needed = guest_count * 2
price_for_eggs = eggs_needed * 0.45
total = price_for_eggs + price_for_breads

if budjet >= total:
    diff = budjet - total
    print(f"Lyubo bought {easter_bread_needed} Easter bread and {eggs_needed} eggs.")
    print(f'He has {diff :.2f} lv. left.')

else:
    diff = total - budjet
    print("Lyubo doesn't have enough money.")
    print(f"He needs {diff :.2f} lv. more.")
