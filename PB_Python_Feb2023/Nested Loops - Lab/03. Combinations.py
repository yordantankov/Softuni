n = int(input())
count = 0
for i in range (0, n + 1):
    for j in range (0, n + 1):
        for x in range (0, n + 1):
            if i + j + x == n:
                count += 1
print(count)