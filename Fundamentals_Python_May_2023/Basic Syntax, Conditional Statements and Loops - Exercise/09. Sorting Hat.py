
while True:

    name = input()
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        exit()
    elif name == "Voldemort":
        print("You must not speak of that name!")
        exit()

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f'{name} goes to Hufflepuff.')