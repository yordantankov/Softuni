from collections import deque

people = input().split(' ')
toss = int(input())
players = deque(people)
i = 1

while len(players) > 1:
    person = players.popleft()

    if i == toss :
        print(f'Removed {person}')
        i = 0
    else:
        players.append(person)
    i += 1

print(f'Last is {players.pop()}')