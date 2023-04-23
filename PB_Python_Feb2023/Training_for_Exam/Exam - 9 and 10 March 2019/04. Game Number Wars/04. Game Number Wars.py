first_player = input()
second_player = input()
player_1_points = 0
player_2_points = 0

while True:
    player_1_card = input()

    if player_1_card == "End of game":
        break
    player_1_card = int(player_1_card)

    player_2_card = int(input())

    if player_1_card > player_2_card:
        diff = player_1_card - player_2_card
        player_1_points+= diff
    elif player_2_card > player_1_card:
        diff = player_2_card - player_1_card
        player_2_points += diff
    elif player_2_card == player_1_card:
        print('Number wars!')
        player_1_card = int(input())
        player_2_card = int(input())
        if player_1_card > player_2_card:
            print(f'{first_player} is winner with {player_1_points} points')
            exit()
        elif player_2_card > player_1_card:
            print(f'{second_player} is winner with {player_2_points} points')
            exit()

print(f'{first_player} has {player_1_points} points')
print(f'{second_player} has {player_2_points} points')

