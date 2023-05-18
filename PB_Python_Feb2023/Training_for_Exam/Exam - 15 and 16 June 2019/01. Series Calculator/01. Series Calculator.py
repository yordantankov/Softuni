import math

serial_name = input()
count_seasons = int(input())
count_episodes = int(input())
time_for_episode_without_ads = float(input())

ads = time_for_episode_without_ads * 0.20
time_with_ads = time_for_episode_without_ads + ads

aditional_time = count_seasons * 10

total = time_with_ads * count_episodes * count_seasons + aditional_time

total = math.floor(total)

print(f"Total time needed to watch the {serial_name} series is {total} minutes.")
