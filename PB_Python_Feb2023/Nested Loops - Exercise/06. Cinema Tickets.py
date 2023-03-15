students_count= 0
standart_count = 0
kid_count = 0
total_tickets = 0
humans_count = 0
while True:
    movie = input()
    if movie == "Finish":
        break

    free_places = int(input())

    for i in range(0 , free_places):
        type_ticket = input()
        if type_ticket == "End":
            break
        elif type_ticket == "student":
            students_count += 1
        elif type_ticket == "standard":
            standart_count += 1
        elif type_ticket == "kid":
            kid_count += 1
        total_tickets += 1
        humans_count += 1

    print(f'{movie} - {humans_count / free_places * 100 :.2f}% full.')
    humans_count = 0


print(f'Total tickets: {total_tickets}')
print(f'{students_count / total_tickets * 100 :.2f}% student tickets.')
print(f'{standart_count / total_tickets * 100 :.2f}% standard tickets.')
print(f'{kid_count / total_tickets * 100 :.2f}% kids tickets.')