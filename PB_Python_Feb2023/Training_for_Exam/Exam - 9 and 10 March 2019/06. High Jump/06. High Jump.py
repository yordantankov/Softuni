henght_to_jump = int(input())
fail_count = 0
total_jumps = 0
first_jump = henght_to_jump - 30

while first_jump <= henght_to_jump:
    jump = int(input())

    if jump > first_jump:
        first_jump += 5
        total_jumps += 1
        fail_count = 0
    elif jump <= first_jump:
        fail_count += 1
        total_jumps += 1

    if fail_count == 3:
        print(f"Tihomir failed at {first_jump}cm after {total_jumps} jumps.")
        exit()

print(f"Tihomir succeeded, he jumped over {henght_to_jump}cm after {total_jumps} jumps.")