def all_types (type,arg):
    if type == "int":
        argument = int(arg)
        argument = argument * 2
        return argument
    elif type == "real":
        argument = float(arg)
        argument = argument * 1.5
        return f'{argument :.2f}'

    elif type == "string":
        return f'${arg}$'


types = input()
argument = input()

print(all_types(types, argument))