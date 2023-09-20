students_count = int(input())
lectures_coutn = int(input())
aditional_bonus = int(input())

max_score = 0
most_atendace = 0

for student in range(students_count):
    atendance = int(input())
    score = (atendance / lectures_coutn) * (5 + aditional_bonus)

    if score > max_score:
        max_score = score
        most_atendace = atendance

print(f"Max Bonus: {round(max_score)}.")
print(f"The student has attended {most_atendace} lectures.")