alien_color = 'green'
if alien_color == 'green':
    print('got 5 point')
elif alien_color == 'yellow':
    print('got 10 print')
else:
    print('got 15 point')

alien_color = 'yellow'
if alien_color == 'green':
    print('got 5 point')
elif alien_color == 'yellow':
    print('got 10 print')
else:
    print('got 15 point')

alien_color = 'red'
if alien_color == 'green':
    print('got 5 point')
elif alien_color == 'yellow':
    print('got 10 print')
else:
    print('got 15 point')


age = 1
if age < 2:
    print('婴儿')
elif age < 4:
    print('幼儿')
elif age < 13:
    print('儿童')
elif age < 20:
    print('青少年')
elif age < 65:
    print('成年人')
else:
    print('老年人')


favorite_fruits = ['apple', 'banana', 'orange']
have_fruits = []
if 'apple' in favorite_fruits:
    have_fruits.append('apple')
if 'peach' in favorite_fruits:
    have_fruits.append('peach')
if 'orange' in favorite_fruits:
    have_fruits.append('orange')
if 'banana' in favorite_fruits:
    have_fruits.append('banana')
if 'lemon' in favorite_fruits:
    have_fruits.append('lemon')

print(have_fruits)