capacity = int(input())
income = 0
people = 0
while True:
    count_people = input()
    if count_people == "Movie time!":
        print(f'There are {capacity} seats left in the cinema.')
        break
    count_people = int(count_people)

    if count_people > capacity:
        print('The cinema is full.')
        break

    income += count_people * 5
    capacity -= count_people
    if count_people % 3 == 0:
        income -= 5

print(f'Cinema income - {income} lv.')