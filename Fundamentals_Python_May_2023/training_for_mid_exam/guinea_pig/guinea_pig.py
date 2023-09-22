food_quantity_in_kg = float(input())
hay_quantity_in_kg = float(input())
cover_quantity_in_kg = float(input())
guineas_weight_in_kg= float(input())

geineas_weight_in_grams = guineas_weight_in_kg * 1000
food_in_grams = food_quantity_in_kg * 1000
hay_in_grams = hay_quantity_in_kg * 1000
cover_in_grams = cover_quantity_in_kg * 1000
puppy_cover = geineas_weight_in_grams / 3
for day in range(1,30+1):
    if food_in_grams >= 300:
        food_in_grams -= 300
    else:
        print("Merry must go to the pet store!")
        exit()
    if day % 2 == 0:
       certain_amount_hay = food_in_grams * 0.05
       if hay_in_grams >= certain_amount_hay:
              hay_in_grams -= certain_amount_hay
       else:
           print("Merry must go to the pet store!")
           exit()

    if day % 3 == 0:
        if cover_in_grams >= puppy_cover:
            cover_in_grams -= puppy_cover
        else:
            print("Merry must go to the pet store!")
            exit()
    if food_in_grams <= 0 or cover_in_grams <= 0 or hay_in_grams <= 0:
        print("Merry must go to the pet store!")
        exit()

print(f"Everything is fine! Puppy is happy! Food: {food_in_grams / 1000 :.2f}, Hay: {hay_in_grams / 1000 :.2f}, Cover: {cover_in_grams / 1000 :.2f}.")