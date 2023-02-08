x = float(input())
y = float (input())
h = float (input())

#green_paint!
side_wall = x * y
window = 1.5 * 1.5
two_of_sides = (2 * side_wall) - (2 * window)
back_wall = x * x
vhod = 1.2 * 2
total_back_and_frond = 2 * back_wall - vhod
total_green_area = two_of_sides + total_back_and_frond
green_paint = total_green_area / 3.4

#red_paint!
total_roof = 2 * (x * y)
triangles = 2 * (x * h/ 2)
total_red_area= total_roof + triangles
red_paint = total_red_area / 4.3

print(f"{green_paint :.2f}")
print(f"{red_paint :.2f}")



