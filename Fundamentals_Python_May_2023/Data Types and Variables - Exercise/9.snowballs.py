number_of_snowballs = int(input())
best_quality = 0
best_weight = 0
best_time = 0
best_value = 0

for i in range(1, number_of_snowballs + 1):
    weight_of_snowball = int(input())
    time = int(input())
    quality_of_snowball = int(input())

    value = (weight_of_snowball / time) ** quality_of_snowball

    if value > best_value:
        best_value = value
        best_quality = quality_of_snowball
        best_weight = weight_of_snowball
        best_time = time

print(f"{best_weight} : {best_time} = {int(best_value)} ({best_quality})")
