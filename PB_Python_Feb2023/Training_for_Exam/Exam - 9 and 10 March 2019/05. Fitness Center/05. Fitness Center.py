back_count = 0
chest_count = 0
legs_count = 0
abs_count = 0
bought_shake = 0
bought_bar = 0
bought_people = 0
work_out_people = 0
count_people = int(input())

for i in range(count_people):

    command = input()
    if command == "Back":
        back_count += 1
        work_out_people += 1
    elif command == "Chest":
        chest_count += 1
        work_out_people += 1
    elif command == "Legs":
        legs_count += 1
        work_out_people += 1
    elif command == "Abs":
        abs_count += 1
        work_out_people += 1
    elif command == "Protein shake":
        bought_shake += 1
        bought_people += 1
    elif command == "Protein bar":
        bought_bar += 1
        bought_people += 1

percent_work_out = work_out_people / count_people * 100
percent_protein_bought = bought_people / count_people * 100

print(f'{back_count} - back')
print(f'{chest_count} - chest')
print(f'{legs_count} - legs')
print(f'{abs_count} - abs')
print(f'{bought_shake} - protein shake')
print(f'{bought_bar} - protein bar')
print(f'{percent_work_out :.2f}% - work out')
print(f'{percent_protein_bought :.2f}% - protein')
