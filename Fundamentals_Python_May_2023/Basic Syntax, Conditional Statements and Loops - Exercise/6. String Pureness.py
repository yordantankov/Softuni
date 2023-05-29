n = int(input())

for i in range(n):
    text = input()
    pure = True
    for j in text:
        if j == ',' or j == "." or j == "_":
            pure = False
            break

    if pure == True :
        print(f'{text} is pure.')
    elif pure == False:
        print(f'{text} is not pure!')