pirate_ship_status = list(map(int, input().split(">")))
war_ship_status = list(map(int, input().split(">")))
max_health_of_section = int(input())

command = input()

while command != "Retire":
    command = command.split()
    action = command[0]

    if action == "Fire":
        index, damage = int(command[1]), int(command[2])
        if index in range(len(war_ship_status)):
            war_ship_status[index] -= damage
            if war_ship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()

    elif action == "Defend":
        start_index, end_index, damage = int(command[1]), int(command[2]), int(command[3])
        if start_index in range(len(pirate_ship_status)):
            if end_index in range(len(pirate_ship_status)):
                for index in range(start_index, end_index + 1):
                    pirate_ship_status[index] -= damage
                    if pirate_ship_status[index] <= 0:
                        print("You lost! The pirate ship has sunken.")
                        exit()

    elif action == "Repair":
        index, health = int(command[1]), int(command[2])
        if index in range(len(pirate_ship_status)):
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > max_health_of_section:
                pirate_ship_status[index] = max_health_of_section

    elif action == "Status":
        count_section = 0
        percent_lower = max_health_of_section * 0.20
        for sections in pirate_ship_status:
            if sections < percent_lower:
                count_section += 1
        print(f'{count_section} sections need repair.')

    command = input()

sum_of_pirate_ship = sum(pirate_ship_status)
sum_of_war_ship = sum(war_ship_status)
print(f"Pirate ship status: {sum_of_pirate_ship}")
print(f"Warship status: {sum_of_war_ship}")
