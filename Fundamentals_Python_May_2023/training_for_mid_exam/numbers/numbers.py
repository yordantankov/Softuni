list_integers = list(map(int, input().split()))

sum_numbers = 0
for number in list_integers:
    sum_numbers += number

average_number = sum_numbers / len(list_integers)
top_numbers = []
for element in list_integers:
    if element > average_number:
        top_numbers.append(element)


if max(list_integers) <= average_number:
    print("No")
    exit()

final_list = []
while len(final_list) < 5:
    final_list.append(max(top_numbers))
    top_numbers.remove(max(top_numbers))
    if len(top_numbers) == 0:
        break

for i in final_list:
    print(i, end=" ")
