number_of_messages = int(input())

for i in range(number_of_messages):
    num = int(input())
    message = ''
    if num == 88:
        message = 'Hello'
    elif num == 86:
        message = 'How are you?'
    elif num > 88:
        message = 'Bye.'
    else:
        message = "GREAT!"
    print(message)