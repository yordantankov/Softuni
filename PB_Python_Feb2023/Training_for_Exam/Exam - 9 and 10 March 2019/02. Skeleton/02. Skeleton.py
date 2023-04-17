import math

minutes = int(input())
seconds = int(input())
lenght = float(input())
seconds_for_100_meters = int(input())

min_in_sec = minutes * 60
time_in_sec = min_in_sec + seconds
slow = lenght / 120

slow = lenght / 120
slowest = slow * 2.5
h = (lenght / 100) * seconds_for_100_meters - slowest
if h <= time_in_sec:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {h :.3f}.")
else:
    diff = h - time_in_sec
    print(f"No, Marin failed! He was {diff :.3f} second slower.")


