def get_next_version(version):
    # Split the version string into three parts
    parts = version
    n1, n2, n3 = map(int, parts)

    # Increment the third number, if it's less than 9
    if n3 < 9:
        n3 += 1
    else:
        n3 = 0
        # Increment the second number, if it's less than 9
        if n2 < 9:
            n2 += 1
        else:
            n2 = 0
            # Increment the first number
            n1 += 1

    # Build the next version string
    next_version = f"{n1}.{n2}.{n3}"
    return next_version


# Example usage
current_version = input().split(".")
next_version = get_next_version(current_version)
print(next_version)