n = int(input())
current = 1

for row in range(1, n + 1):

    for col in range(1, row + 1):
        if current > n:
            break

        print(str(current) + " ", end= "")
        current += 1
    print()


