team_name = input()
played_matches = int(input())
total_points = 0
wins = 0
draw = 0
lose = 0
if played_matches == 0:
    print(f"{team_name} hasn't played any games during this season.")
    exit()

for i in range (played_matches):
    result = input()
    if result == "W":
        wins += 1
        total_points += 3
    elif result == "D":
        draw += 1
        total_points += 1
    elif result == "L":
        lose += 1

print(f"{team_name} has won {total_points} points during this season.")
print("Total stats:")
print(f'## W: {wins}')
print(f'## D: {draw}')
print(f'## L: {lose}')
print(f'Win rate: {wins / played_matches * 100 :.2f}%')