first_emplpoyee = int(input())
second_emplpoyee = int(input())
third_emplpoyee = int(input())
students_count = int(input())
needed_hours = 0
all_employees_answering_per_hour = first_emplpoyee + second_emplpoyee + third_emplpoyee

while students_count > 0:
    needed_hours += 1

    if needed_hours % 4 == 0:
        continue
    students_count -= all_employees_answering_per_hour
    if students_count == 0:
        break


print(f'Time needed: {needed_hours}h.')


