n = int(input())
capacity = 0
for i in range(n):
    liters = int(input())
    if liters>= 255:
        print('Insufficient capacity!')
        continue
    elif capacity + liters > 255:
        print('Insufficient capacity!')
        continue
    else:
        capacity+= liters
print(capacity)