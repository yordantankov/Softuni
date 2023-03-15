n = int(input())
for i in range (1 , 9+1):
    for j in range (1, 9+1):
        for x in range(1, 9+1):
            for k in range (1,9+1):
                if n % i == 0 and n % j == 0 and n % x == 0 and n % k == 0:
                    print(f'{i}{j}{x}{k}', end=" ")