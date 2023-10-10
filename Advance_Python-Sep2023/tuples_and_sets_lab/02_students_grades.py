n = int(input())
students ={}

for _ in range(n):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for students_name, grades in students.items():
    formated_grades = ' '.join([f"{grade:.2f}" for grade in grades])
    print(f"{students_name} -> {formated_grades} (avg: {sum(grades) / len(grades) :.2f})")
