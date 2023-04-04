import sys

top_player = ""
top_goals = -sys.maxsize

while True:
    player = input()
    if player == "END":
        break
    goals = int(input())
    if goals > top_goals:
        top_goals = goals
        top_player = player

    if goals >= 10:
        top_goals = goals
        print(f'{top_player} is the best player!')
        print(f'He has scored {top_goals} goals and made a hat-trick !!!')
        exit()


print(f"{top_player} is the best player!")
if top_goals >= 3:
    print(f"He has scored {top_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {top_goals} goals.")


