dict_of_students = {}
while True:
    given_name = input()
    if ":" not in given_name:
        last_course = given_name
        break
    given_name = given_name.split(":")
    name = given_name[0]
    score = int(given_name[1])
    course = given_name[2]
    dict_of_students[name] = score, course

for student in dict_of_students:
    course = dict_of_students[student]
    name_of_course = course[1]
    if last_course[0:3] == name_of_course[0:3]:
        score = dict_of_students[student]
        print(f"{student} - {score[0]}")