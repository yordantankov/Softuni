easter_breads = int(input())
top_chef = ""
top_score = 0
score = 0

for i in range(easter_breads):
    chef_name = input()

    while True:

        grade = input()

        if grade == "Stop":
            break

        grade = int(grade)
        score += grade

    print(f"{chef_name} has {score} points.")
    if score > top_score:
        top_score = score
        top_chef = chef_name
        print(f"{top_chef} is the new number 1!")

    score = 0

print(f"{top_chef} won competition with {top_score} points!")