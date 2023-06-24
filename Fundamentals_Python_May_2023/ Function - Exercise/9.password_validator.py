def password_validation (some_pass):
    is_valid = True
    if len(some_pass) < 6 or len(some_pass) > 10:
         print("Password must be between 6 and 10 characters")
         is_valid = False
    if not some_pass.isalnum():
         print(f"Password must consist only of letters and digits")
         is_valid = False

    count_digits =0
    for character in some_pass:
        if character.isdigit():
             count_digits += 1

    if count_digits < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    return is_valid

password = input()
password_is_valid = password_validation(password)

if password_is_valid:
    print("Password is valid")