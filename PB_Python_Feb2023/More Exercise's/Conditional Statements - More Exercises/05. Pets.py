import math

days = int(input())
food_for_pets = int(input())
food_for_dog = float(input())
food_for_cat = float(input())
food_for_turtle = float(input())

dog_eaten = days * food_for_dog
cat_eaten = days * food_for_cat
turtle_eaten = days * food_for_turtle / 1000

all_eaten = dog_eaten + cat_eaten + turtle_eaten

if all_eaten <= food_for_pets :
    food_for_pets -= all_eaten
    print(f"{math.floor(food_for_pets)} kilos of food left.")
else:
    all_eaten-= food_for_pets
    print(f'{math.ceil(all_eaten)} more kilos of food are needed.')