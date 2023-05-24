budget = float(input())
salary = 0

while True:
    actor_name = input()
    if actor_name == "ACTION":
        break

    if len(actor_name) > 15:
        salary = budget * 0.20
        budget -= salary
    else:
        sal = float(input())
        budget -= sal

    if budget <= 0:
        print(f"We need {abs(budget) :.2f} leva for our actors.")
        exit()

print(f"We are left with {budget :.2f} leva.")