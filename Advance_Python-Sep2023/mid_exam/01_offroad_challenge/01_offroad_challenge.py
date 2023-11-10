initial_fuel = list(map(int, input().split()))
consumption = list(map(int, input().split()))
need_fuel = list(map(int, input().split()))

reached_altitudes = []
failed_altitudes = []

for altitude in need_fuel:
    current_fuel = initial_fuel[-1]
    consumption = consumption[0]

    if current_fuel - consumption >= altitude:
        reached_altitudes.append(altitude)
        initial_fuel.pop()
        consumption.pop(0)
    else:
        failed_altitudes.append(altitude)
        break

if not need_fuel:
    print("John has reached all the altitudes and managed to reach the top!")
else:
    for i, altitude in enumerate(reached_altitudes, start=1):
        print(f"John has reached: Altitude {i}")

    for i, altitude in enumerate(failed_altitudes, start=len(reached_altitudes) + 1):
        print(f"John did not reach: Altitude {i}")

    if reached_altitudes:
        print("John failed to reach the top.")
        print(f"Reached altitudes: {'Altitude ' + ', Altitude '.join(map(str, range(1, len(reached_altitudes) + 1)))}")
    else:
        print("John failed to reach the top.")
        if failed_altitudes:
            print("John didn't reach any altitude.")