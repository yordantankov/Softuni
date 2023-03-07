name = input()
average_grade = 0
now_grade = 1
fail_count = 0

while now_grade <= 12:
    grade = float(input())
    if grade < 4.00:
        if fail_count == 1:
            print(f'{name} has been excluded at {now_grade} grade')
            exit()
        
        fail_count += 1
        continue

    average_grade += grade
    if now_grade == 12:
        break
    now_grade += 1


average_grade = average_grade / now_grade
print(f'{name} graduated. Average grade: {average_grade :.2f}')