students_qty = int(input())

average_succes = 0
top_students = 0
between_4_and_5 = 0
between_3_and_4= 0
fails_students = 0

for i in range (0, students_qty):
    grade = float(input())

    if grade >= 5.00 :
        top_students += 1
    elif grade >= 4.00 and grade < 5.00:
        between_4_and_5 += 1
    elif grade >= 3.00 and grade < 4.00:
        between_3_and_4 += 1
    elif grade >= 2.00 and grade < 3.00:
        fails_students += 1
    average_succes += grade

print(f'Top students: {top_students / students_qty * 100 :.2f}%')
print(f'Between 4.00 and 4.99: {between_4_and_5 / students_qty * 100 :.2f}%')
print(f'Between 3.00 and 3.99: {between_3_and_4 / students_qty * 100 :.2f}%')
print(f'Fail: {fails_students / students_qty * 100 :.2f}%')
print(f'Average: {average_succes / students_qty  :.2f}')
