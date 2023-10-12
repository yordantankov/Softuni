n =  int(input())

unique_names = set()
a = []

for i in range(n):
    name = input()
    unique_names.add(name)

for name in unique_names:
    print(name)