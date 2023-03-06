import sys
command = input()
min_num = sys.maxsize

while command != "Stop":
    command = int(command)
    if command < min_num:
        min_num = command
    command = input()

print(min_num)