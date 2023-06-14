initial_energy = 100
initial_coins = 100

events = input().split("|")
factory_is_open = True
for event in events:
    event_items = event.split("-")
    task = event_items[0]
    count = int(event_items[1])

    if task == "rest":
        curren_energy = initial_energy
        initial_energy += count
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - curren_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")

    elif task == 'order':
         if initial_energy >= 30 :
             initial_energy -= 30
             print(f"You earned {count} coins.")
             initial_coins += count
         else:
             initial_energy += 50
             print('You had to rest!')

    else:
        if initial_coins >= count:
            print(f'You bought {task}.')
            initial_coins -= count
        else:
             factory_is_open = False
             break
if factory_is_open:
    print('Day completed!')
    print(f'Coins: {initial_coins}')
    print(f'Energy: {initial_energy}')
else:
    print(f"Closed! Cannot afford {task}.")