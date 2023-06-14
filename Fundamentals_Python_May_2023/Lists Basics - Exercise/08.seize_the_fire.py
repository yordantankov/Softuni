cells = input().split("#")
water_tank_capacity = int(input())
cell_is_valid = False
High = range(81, 125+ 1)
Medium = range(51, 80+1)
Low = range(1, 50+1)
effort = 0
total_fire = 0
out_fires = []
for cell in cells:
    type_of_fire, value_of_cell = cell.split(' = ')
    value_of_cell = float(value_of_cell)
    cell_is_valid = False
    if type_of_fire == "High":
        if value_of_cell in High:
            cell_is_valid = True

    elif type_of_fire == "Medium":
            if value_of_cell in Medium:
                cell_is_valid = True

    elif type_of_fire == "Low":
            if value_of_cell in Low:
                cell_is_valid = True

    if cell_is_valid:
        if value_of_cell <= water_tank_capacity:
            water_tank_capacity -= value_of_cell
            effort += value_of_cell * 0.25
            out_fires.append(value_of_cell)
            total_fire += value_of_cell

print('Cells:')
for out_fire in out_fires:
    print(f' - {int(out_fire)}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {int(total_fire)}')
