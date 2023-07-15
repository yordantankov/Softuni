price_ratings = list(map(int, input().split(", ")))
entry_point = int(input())
item_type = input()

left_sum = 0
right_sum = 0

for element in range(entry_point - 1, -1, -1):
    if item_type == "cheap" and price_ratings[element] < price_ratings[entry_point]:
        left_sum += int(price_ratings[element])

    elif item_type == "expensive" and price_ratings[element] >= price_ratings[entry_point]:
        left_sum += price_ratings[element]

for element in range(entry_point + 1, len(price_ratings)):
    if item_type == "cheap" and price_ratings[element] < price_ratings[entry_point]:
        right_sum += price_ratings[element]

    elif item_type == "expensive" and price_ratings[element] >= price_ratings[entry_point]:
        right_sum += price_ratings[element]

if left_sum >= right_sum:
    print(f"Left - {left_sum}")
else:
    print(f"Right - {right_sum}")