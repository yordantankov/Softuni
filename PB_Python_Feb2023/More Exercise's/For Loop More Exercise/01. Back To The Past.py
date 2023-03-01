money = float(input())
year_to_live = int(input())
years = 18

for i in range(1800, year_to_live + 1):
    if i % 2 == 0:
        money -= 12000
    else :
        money -= 12000 + 50 * years
    years += 1

if money >= 0 :
    print(f"Yes! He will live a carefree life and will have {money :.2f} dollars left." )
else:
    diff = abs(money)
    print(f"He will need {diff :.2f} dollars to survive.")