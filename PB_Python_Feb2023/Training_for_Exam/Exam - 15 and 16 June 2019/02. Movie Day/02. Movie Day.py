time_for_shots = int(input())
scenes_qty = int(input())
time_for_scene = int(input())

preparing = round(time_for_shots * 0.15)
time_for_all_shots = scenes_qty * time_for_scene
total_time = time_for_all_shots + preparing

if total_time <= time_for_shots:
    diff = time_for_shots - total_time
    diff = int(diff)
    print(f"You managed to finish the movie on time! You have {diff} minutes left!")
else:
    diff = abs(time_for_shots - total_time)
    print(f"Time is up! To complete the movie you need {diff} minutes.")