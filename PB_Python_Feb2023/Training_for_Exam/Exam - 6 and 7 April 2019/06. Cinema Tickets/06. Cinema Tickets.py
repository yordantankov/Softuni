
total_tickets = 0
student_qty = 0
standard_qty = 0
kid_qty = 0
tickets_for_projection = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        break

    free_places = int(input())
    for i in range(0 , free_places):
        type_ticket = input()
        if type_ticket == "End":
            break

        if type_ticket == "student":
            student_qty += 1
        elif type_ticket == "standard":
            standard_qty += 1
        elif type_ticket == "kid":
            kid_qty += 1
        total_tickets += 1
        tickets_for_projection += 1

    print(f'{movie_name} - {tickets_for_projection / free_places * 100 :.2f}% full.')
    tickets_for_projection = 0


print(f'Total tickets: {total_tickets}')
print(f'{student_qty / total_tickets * 100 :.2f}% student tickets.')
print(f'{standard_qty / total_tickets * 100 :.2f}% standard tickets.')
print(f'{kid_qty / total_tickets * 100 :.2f}% kids tickets.')



