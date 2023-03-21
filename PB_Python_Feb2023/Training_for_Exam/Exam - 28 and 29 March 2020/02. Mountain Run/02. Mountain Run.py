import math

world_record = float(input())
meters = float(input())
time_for_one_meter = float(input())

time_for_finish = meters * time_for_one_meter
slowest_time = math.floor(meters / 50) * 30
total_time = time_for_finish + slowest_time

if total_time < world_record:
    print(f"Yes! The new record is {total_time :.2f} seconds.")
else:
    diff = total_time - world_record
    print(f'No! He was {diff :.2f} seconds slower.')
