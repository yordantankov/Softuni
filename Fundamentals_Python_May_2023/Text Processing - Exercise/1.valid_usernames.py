given_usernames = input().split(", ")

for username in given_usernames:
    if len(username) >= 3 and len(username) <= 16:
        if " " not in username:
            if username.isalnum() or "-" in username or "_" in username:
                print(username)

