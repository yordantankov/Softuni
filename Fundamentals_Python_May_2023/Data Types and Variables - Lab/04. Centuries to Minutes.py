centuries = int(input())

years = centuries * 100
days = int(years * 365.24220)
hours = int(days * 24)
min = int(hours * 60)

print(f'{centuries} centuries = {int(years)} years = {int(days)} days = {int(hours)} hours = {int(min)} minutes')