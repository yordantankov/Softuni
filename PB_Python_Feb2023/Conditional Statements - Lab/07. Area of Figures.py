import math

type_fig = input()

if type_fig == "square":
    lenght = float(input())
    face = lenght * lenght
    print(f"{face :.3f}")

elif type_fig == "rectangle":
    a = float(input())
    b = float (input())
    face = a * b
    print(f"{face :.3f}")


elif type_fig == "circle":
    radius = float(input())
    face = math.pi * (radius ** 2)
    print(f"{face :.3f}")

elif type_fig == "triangle" :
    lengt = float (input())
    side = float (input())
    face = lengt * side / 2
    print (f"{face :.3f}")
