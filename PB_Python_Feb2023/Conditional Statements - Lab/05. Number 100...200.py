price_vacation = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

price = puzzles * 2.60 + dolls * 3 + bears * 4.10 + minions * 8.20 + trucks * 2
number_of_toys = puzzles + dolls + bears + minions + trucks

if number_of_toys >= 50:
    price *= 0.75

price *= 0.90

if price > price_vacation:
    print(f"Yes! {price - price_vacation:.2f} lv left.")
else:
    print(f"Not enough money! {price_vacation - price:.2f} lv needed.")