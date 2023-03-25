bought_food = int(input())
food_in_grams = bought_food * 1000
while True:
    grams_eaten = input()
    if grams_eaten == "Adopted":
        break

    grams_eaten = int(grams_eaten)
    food_in_grams -= grams_eaten


if food_in_grams < 0:
    food_in_grams = abs(food_in_grams)
    print(f'Food is not enough. You need {food_in_grams} grams more.')


else:
   print(f'Food is enough! Leftovers: {food_in_grams} grams.')