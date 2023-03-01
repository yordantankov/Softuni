groups_qty = int(input())

musala_mem = 0
monblan_mem = 0
kilimanjaro_mem = 0
k2_mem = 0
everest_mem = 0
all_mem = 0

for i in range(0, groups_qty):
    members_in_group = int(input())
    if members_in_group >= 1 and members_in_group <= 5:
        musala_mem += members_in_group
    elif members_in_group > 5 and members_in_group <= 12:
        monblan_mem += members_in_group
    elif members_in_group > 12 and members_in_group <= 25:
        kilimanjaro_mem += members_in_group
    elif members_in_group > 25 and members_in_group <= 40:
        k2_mem += members_in_group
    else:
        everest_mem += members_in_group
    all_mem += members_in_group

print(f'{((musala_mem / all_mem) * 100) :.2f}%')
print(f'{((monblan_mem / all_mem) * 100) :.2f}%')
print(f'{((kilimanjaro_mem / all_mem) * 100) :.2f}%')
print(f'{((k2_mem / all_mem) * 100) :.2f}%')
print(f'{((everest_mem / all_mem) * 100) :.2f}%')


