season = input()
kilometers = float(input())
salary = 0

if kilometers <= 5000 :
    if season == "Spring" or season == "Autumn" :
        salary = kilometers * 0.75
    elif season == "Summer" :
        salary = kilometers * 0.90
    elif season == "Winter" :
        salary = kilometers * 1.05

elif kilometers > 5000 and kilometers <= 10000 :
    if season == "Spring" or season == "Autumn" :
        salary = kilometers * 0.95
    elif season == "Summer" :
        salary = kilometers * 1.10
    elif season == "Winter" :
        salary = kilometers * 1.25

elif kilometers > 10000 :
    salary = kilometers * 1.45

sum = salary * 4
total_sum = sum - (sum * 0.10)
print(f"{total_sum :.2f}")
