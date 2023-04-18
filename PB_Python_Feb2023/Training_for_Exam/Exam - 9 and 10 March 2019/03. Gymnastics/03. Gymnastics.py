country = input()
tool = input()
hardnes = 0
grade = 0
if country == "Russia":
    if tool == "ribbon":
        hardnes = 9.100
        grade = 9.400
    elif tool == "hoop":
        hardnes = 9.300
        grade = 9.800
    elif tool == "rope":
        hardnes = 9.600
        grade = 9.000

elif country == "Bulgaria":
    if tool == "ribbon":
        hardnes = 9.600
        grade = 9.400
    elif tool == "hoop":
        hardnes = 9.550
        grade = 9.750
    elif tool == "rope":
        hardnes = 9.500
        grade = 9.400

elif country == "Italy":
    if tool == "ribbon":
        hardnes = 9.200
        grade = 9.500
    elif tool == "hoop":
        hardnes = 9.450
        grade = 9.350
    elif tool == "rope":
        hardnes = 9.700
        grade = 9.150

total_grade_country = hardnes + grade
left_grade = 20 - total_grade_country
percent = (left_grade / 20) * 100

print(f"The team of {country} get {total_grade_country :.3f} on {tool}.")
print(f"{percent :.2f}%")