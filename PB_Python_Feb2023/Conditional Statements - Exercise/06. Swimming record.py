import math

world_record = float(input())
meters_to_swim = float(input())
time_for_1_meter = float(input())

time_to_swim = meters_to_swim * time_for_1_meter
slowest_time = math.floor(meters_to_swim / 15)
slow_time = slowest_time * 12.5
total_time = time_to_swim + slow_time


if total_time >= world_record:
    total_time-= world_record
    print(f'No, he failed! He was {total_time :.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {total_time :.2f} seconds.')