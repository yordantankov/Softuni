actor_name = input()
start_point = float(input())
appreciative_persons = int(input())
points = 0

for i in range (0, appreciative_persons):
    apprec_person_name = input()
    points_appreciate = float (input())
    start_point += (len(apprec_person_name) * points_appreciate) / 2
    if start_point > 1250.50:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {start_point :.1f}!')
        exit()

print(f'Sorry, {actor_name} you need {(1250.5 - start_point) :.1f} more!')