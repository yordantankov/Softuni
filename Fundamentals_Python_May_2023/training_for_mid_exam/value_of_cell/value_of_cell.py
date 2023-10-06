
fire_cells = input().split("#")
water = int(input())
is_valid_range = False
effort = 0
seized_cells = []
high = range(81, 125+1)
medium = range(51, 81+1)
low = range(1, 50+1)
total_fire = 0
out_fires = []
for element in fire_cells:
    type_of_fire, value_of_cell = element.split(' = ')
    value_of_cell = float(value_of_cell)

    if type_of_fire == "High":
        if value_of_cell in high:
            is_valid_range = True
    elif type_of_fire == "Medium":
        if value_of_cell in medium:
            is_valid_range = True
    elif type_of_fire == "Low":
        if value_of_cell in low:
            is_valid_range = True


    if is_valid_range:
        if value_of_cell <= water:
            water -= value_of_cell
            effort += value_of_cell * 0.25
            out_fires.append(value_of_cell)
            total_fire += value_of_cell


print("Cells:")

for out in out_fires:
    print(f"- {int(out)}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {int(total_fire)}")