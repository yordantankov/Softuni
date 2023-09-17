def enroll_hero(heroes, hero_name):
    if hero_name in heroes:
        print(f"{hero_name} is already enrolled.")
    else:
        heroes[hero_name] = []


def learn_spell(heroes, hero_name, spell_name):
    if hero_name not in heroes:
        print(f"{hero_name} doesn't exist.")
    elif spell_name in heroes[hero_name]:
        print(f"{hero_name} has already learnt {spell_name}.")
    else:
        heroes[hero_name].append(spell_name)


def unlearn_spell(heroes, hero_name, spell_name):
    if hero_name not in heroes:
        print(f"{hero_name} doesn't exist.")
    elif spell_name not in heroes[hero_name]:
        print(f"{hero_name} doesn't know {spell_name}.")
    else:
        heroes[hero_name].remove(spell_name)


def print_heroes(heroes):
    print("Heroes:")
    for hero, spells in heroes.items():
        spells_str = ", ".join(spells)
        print(f"== {hero}: {spells_str}")


def main():
    heroes = {}

    while True:
        command = input().strip().split()
        if command[0] == "End":
            break

        action = command[0]
        hero_name = command[1]

        if action == "Enroll":
            enroll_hero(heroes, hero_name)
        elif action == "Learn":
            spell_name = command[2]
            learn_spell(heroes, hero_name, spell_name)
        elif action == "Unlearn":
            spell_name = command[2]
            unlearn_spell(heroes, hero_name, spell_name)

    print_heroes(heroes)


if __name__ == "__main__":
    main()

