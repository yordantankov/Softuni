days_of_tournaments = int(input())
wins_count = 0
lose_count = 0
money_earned = 0
total_money = 0
total_wins = 0
total_loses = 0
for i in range(0, days_of_tournaments):

    while True:
        sport = input()
        if sport == "Finish":
            break
        result = input()

        if result == "win":
            wins_count += 1
            total_wins += 1
            money_earned += 20
        elif result == "lose":
            lose_count += 1
            total_loses += 1

    if wins_count > lose_count:
        money_earned += money_earned * 0.10
    wins_count = 0
    lose_count = 0
    total_money+= money_earned
    money_earned = 0

if total_wins > total_loses:
    total_money += total_money * 0.20
    print(f"You won the tournament! Total raised money: {total_money :.2f}")

else:
    print(f"You lost the tournament! Total raised money: {total_money :.2f}")
