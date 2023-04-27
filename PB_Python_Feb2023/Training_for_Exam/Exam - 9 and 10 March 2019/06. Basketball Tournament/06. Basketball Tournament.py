win_mathes  = 0
lose_mathes = 0
total_mathes = 0
while True:
    tournament_name = input()
    if tournament_name == "End of tournaments":
        break

    mathes = int(input())

    for i in range (1, mathes + 1):
        first_squad_points = int(input())
        second_squad_points = int(input())

        if first_squad_points > second_squad_points:
            diff = first_squad_points - second_squad_points
            win_mathes += 1
            total_mathes += 1
            print(f'Game {i} of tournament {tournament_name}: win with {diff} points.')

        elif second_squad_points > first_squad_points:
            diff = second_squad_points - first_squad_points
            lose_mathes += 1
            total_mathes += 1
            print(f"Game {i} of tournament {tournament_name}: lost with {diff} points.")


percent_wins = win_mathes / total_mathes * 100
percent_lose = lose_mathes / total_mathes * 100
print(f'{percent_wins :.2f}% matches win')
print(f'{percent_lose :.2f}% matches lost')

