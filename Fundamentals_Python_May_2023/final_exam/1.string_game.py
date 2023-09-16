def execute_commands(input_str, commands):
    for command in commands:
        if command[0] == "Change":
            char, replacement = command[1], command[2]
            input_str = input_str.replace(char, replacement)
            print(input_str)
        elif command[0] == "Includes":
            substring = command[1]
            print("True" if substring in input_str else "False")
        elif command[0] == "End":
            substring = command[1]
            print("True" if input_str.endswith(substring) else "False")
        elif command[0] == "Uppercase":
            input_str = input_str.upper()
            print(input_str)
        elif command[0] == "FindIndex":
            char = command[1]
            index = input_str.find(char)
            print(index)
        elif command[0] == "Cut":
            start_index, count = int(command[1]), int(command[2])
            cut_chars = input_str[start_index:start_index + count]
            print(cut_chars)


def main():
    input_str = input().strip()
    commands = []

    while True:
        command = input().strip().split()
        if command[0] == "Done":
            break
        commands.append(command)

    execute_commands(input_str, commands)


if __name__ == "__main__":
    main()
