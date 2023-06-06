count_people = int(input())
capacity = int(input())
courses = 0
left_people = 0
while True:
    if count_people <= 0:
        break
    if count_people <= capacity:

        courses += 1
        count_people -= capacity

    elif count_people > capacity:
        courses += 1
        count_people -= capacity

print(courses)
