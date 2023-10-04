# guest_name = input('Input your name please: ')
# with open('guest.txt', 'w') as file_object:
#     file_object.write(guest_name)

while True:
    guest_name = input('Input your name please: ')
    if guest_name == 'q':
        print('See you!')
        break
    with open('guest_book.txt', 'a') as file_object:
        file_object.write(guest_name + '\n')
    print(f'Welcome, {guest_name.title()}')

while True:
    reason = input('Input the reason why you like programing: ')
    if reason == 'q':
        break
    with open('reason.txt', 'a', encoding='UTF-8') as file_object:
        file_object.write(reason + '\n')
