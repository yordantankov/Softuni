import math

serial_name = input()
episode_time = int(input())
rest_time = int(input())

lunch_time = rest_time / 8
relax_time = rest_time / 4

total_time =rest_time - lunch_time - relax_time

if total_time >= episode_time :
    total_time-=episode_time
    print(f'You have enough time to watch {serial_name} and left with {math.ceil(total_time)} minutes free time.')
else:
    episode_time -= total_time
    print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(episode_time)} more minutes.")