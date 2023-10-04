print('#5-08')
users = ['admin', 'user01', 'user02', 'user03', 'user04']
for user in users:
    if user == 'admin':
        print('Hello, admin. would you like to see a status report?')
    else:
        print(f"Hello {user}, thank you for logging in again.")

print('#5-09')
users = []
if users:
    for user in users:
        if user == 'admin':
            print('Hello, admin. would you like to see a status report?')
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print('We need to find some users!')


print('#5-10')
current_users = ['admin', 'uSer01', 'user02', 'user03', 'user04']
new_users = ['Admin', 'User01', 'user05', 'user06', 'user07']
current2_users = [current2_user.lower() for current2_user in current_users[:]]
for new_user in new_users:
    if new_user.lower() in current2_users:
        print(f'username {new_user} is exist')
    else:
        print(f'username {new_user} is available')

print('#5-11')
lists = list(range(1,10))
for num in lists:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print('3rd')
    else:
        print(f'{num}th')
