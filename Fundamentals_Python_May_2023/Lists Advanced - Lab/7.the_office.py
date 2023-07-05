int_employees = list(map(int, input().split()))
happiness_to_multiply = int(input())

employeed_hapiness = []
for employee in int_employees:
    employeed_hapiness.append(employee * happiness_to_multiply)

average_happiness = sum(employeed_hapiness) / len(employeed_hapiness)

filtered_employees = []
for employe in employeed_hapiness:
    if employe >= average_happiness:
        filtered_employees.append(employe)

if len(filtered_employees) >= len(employeed_hapiness) / 2:
    print(f"Score: {len(filtered_employees)}/{len(employeed_hapiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_employees)}/{len(employeed_hapiness)}. Employees are not happy!")