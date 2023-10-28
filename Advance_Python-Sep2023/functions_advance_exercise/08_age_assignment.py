def age_assignment(*args, **kwargs):
    person = {}
    for name in args:
        person[name] = kwargs[name[0]]
    result = sorted(person.items(), key=lambda x: x[0])
    final_result = []
    for name, age in result:
        final_result.append(f"{name} is {age} years old.")

    return "\n".join(final_result)


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
