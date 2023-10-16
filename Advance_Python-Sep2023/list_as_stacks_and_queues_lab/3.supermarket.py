from collections import deque

remaining = deque()
command = input()

while command != "End":
    if command == "Paid":
        while len(remaining):
            print(remaining.popleft())

    else:
        remaining.append(command)
    command = input()

print(f"{len(remaining)} people remaining.")
