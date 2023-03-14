juri = int(input())
total_grades = 0
presentation_count = 0
all_grades = 0
while True:
    presentation_name = input()
    if presentation_name == "Finish":
        break

    for i in range (0, juri):
        grade = float(input())
        total_grades += grade
        all_grades += grade
        presentation_count += 1

    average_grade = total_grades / juri
    print(f'{presentation_name} - {average_grade :.2f}.')
    total_grades = 0

print(f"Student's final assessment is {all_grades / presentation_count :.2f}.")