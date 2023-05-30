while True:
    text = input()
    if text == "SoftUni":
        continue
    elif text == "End":
        exit()

    for i in text:
        print(i * 2, end="")

    print()
