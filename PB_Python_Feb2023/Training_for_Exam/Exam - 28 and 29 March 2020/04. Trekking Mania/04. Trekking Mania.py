count_groups = int(input())
count_Musala = 0
count_Monblan = 0
count_kilimandjaro = 0
count_K2 = 0
count_Everest = 0
total_people = 0

for i in range(0, count_groups):
    people = int(input())

    if people <= 5:
        count_Musala += people
    elif people > 5 and people < 13 :
        count_Monblan += people
    elif people >= 13 and people <= 25 :
        count_kilimandjaro += people
    elif people > 25 and people <= 40:
        count_K2 += people
    elif people > 40:
        count_Everest += people

    total_people += people

print(f'{count_Musala / total_people * 100 :.2f}%')
print(f'{count_Monblan / total_people * 100 :.2f}%')
print(f'{count_kilimandjaro / total_people * 100 :.2f}%')
print(f'{count_K2 / total_people * 100 :.2f}%')
print(f'{count_Everest / total_people * 100 :.2f}%')


