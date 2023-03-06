import sys
command = input()
max_num = -sys.maxsize

while command != "Stop":
    command = int(command)
    if command > max_num:
        max_num = command
    command = input()
print(max_num)