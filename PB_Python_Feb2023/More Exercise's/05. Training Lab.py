import math

lenght = float(input())
widht = float (input())

rows= math.floor ((lenght * 100) / 120)
desks = math.floor(((widht *100)-100) / 70)
numbers = rows * desks - 3
print (numbers)