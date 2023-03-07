fail_score = int(input())
fail_count = 0
average_score = 0
num_of_problems = 0
last_problem = ''
while True:
    task_name = input()
    if task_name == "Enough":
        break
    grade = int(input())

    if task_name != last_problem:
        last_problem = task_name

    if grade <= 4 :
        fail_count += 1
        if fail_count == fail_score:
            print(f'You need a break, {fail_count} poor grades.')
            exit()

    num_of_problems += 1
    average_score += grade

average_score = average_score / num_of_problems

print(f'Average score: {average_score :.2f}')
print(f'Number of problems: {num_of_problems}')
print(f'Last problem: {last_problem}')