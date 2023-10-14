n = int(input())
chemicals = set()
for _ in range(n):
    element = input().split()
    for el in element:
        chemicals.add(el)

for el in chemicals:
    print(el)