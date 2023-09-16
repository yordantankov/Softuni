input_string = input()
processed_string = ""
explosion_strength = 0

for char in input_string:
    if char == '>':
        processed_string += char
        explosion_strength = 0
    elif char.isdigit():
        explosion_strength += int(char)
    else:
        if explosion_strength == 0:
            processed_string += char
        else:
            if explosion_strength == 1:
                explosion_strength -= 1
            else:
                explosion_strength -= 1
                continue

print(processed_string)