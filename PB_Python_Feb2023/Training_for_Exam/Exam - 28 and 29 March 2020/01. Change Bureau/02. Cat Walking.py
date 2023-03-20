minutes_walk_a_day = int(input())
count_walks = int(input())
calories_have_a_day = int(input())

total_minutes = minutes_walk_a_day * count_walks
burned_calories = total_minutes * 5

if burned_calories >= calories_have_a_day / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")

elif burned_calories <= calories_have_a_day / 2:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")

