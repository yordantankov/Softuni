days = int(input())
total_food = float(input())
dog_eaten = 0
cat_eaten = 0
count_days = 0
biscuit_total = 0
total_eat = 0
eat_for_the_day = 0

for i in range(0, days):

    dog_eat = int(input())
    cat_eat = int(input())
    count_days += 1
    dog_eaten += dog_eat
    cat_eaten += cat_eat
    total_eat += dog_eat + cat_eat

    if count_days == 3:
        count_days = 0
        eat_for_the_day = dog_eat + cat_eat
        biscuit_total += eat_for_the_day * 0.10

biscuit_total = round(biscuit_total)
print(f'Total eaten biscuits: {biscuit_total}gr.')
print(f'{total_eat / total_food * 100 :.2f}% of the food has been eaten.')
print(f'{dog_eaten / total_eat * 100 :.2f}% eaten from the dog.')
print(f'{cat_eaten / total_eat * 100 :.2f}% eaten from the cat.')