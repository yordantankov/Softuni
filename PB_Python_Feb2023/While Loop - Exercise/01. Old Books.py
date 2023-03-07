fav_book = input()
count_books = 0

book_checked = input()
while book_checked != "No More Books":

    if book_checked == fav_book:
        print(f'You checked {count_books} books and found it.')
        exit()
    count_books += 1
    book_checked = input()

print("The book you search is not here!")
print(f'You checked {count_books} books.')