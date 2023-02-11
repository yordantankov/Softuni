

volume = int(input())
p1 = int(input())
p2 = int(input())
hours = float(input())

capacity_p1 = p1 * hours
capacity_p2 = p2 * hours
total_water = capacity_p2 + capacity_p1

if total_water > volume:
    ostatak = total_water - volume
    print (f"For {hours} hours the pool overflows with {ostatak} liters.")
else :
    percent_total_water = (total_water / volume) *100
    p1_percent = capacity_p1 / total_water * 100
    p2_percent = capacity_p2 / total_water * 100

    print (f"The pool is {percent_total_water}% full. Pipe 1: {p1_percent}%. Pipe 2: {p2_percent}%.")



