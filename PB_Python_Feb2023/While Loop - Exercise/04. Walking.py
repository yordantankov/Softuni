steps_goal = 10000
count_steps = 0

while True :
    steps = input()

    if steps == "Going home":
        steps = int(input())
        count_steps += steps

        if count_steps >= steps_goal:
            break
        elif count_steps < steps_goal:
            diff = steps_goal - count_steps
            print(f'{diff} more steps to reach goal.')
            exit()

    steps = int(steps)
    count_steps += steps
    if count_steps >= steps_goal:
        break

diff = count_steps - steps_goal
print('Goal reached! Good job!')
print(f'{diff} steps over the goal!')
