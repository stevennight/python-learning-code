print("#4-10")
list1 = list(range(1, 11))
print(list1 )
print("The first three items in the list are:")
for item in list1[:3]:
    print(item)
print("Three items from the middle of the list are:")
middle = round(len(list1) / 2) - 1
for item in list1[middle - 1:middle + 2]:
    print(item)
print("The last three items in the list are:")
for item in list1[-3:]:
    print(item)

print('#4-11')
pizzas = ['p1', 'p2', 'p3']
friend_pizzas = pizzas[:]
pizzas.append('p4')
friend_pizzas.append('p-4')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

print("#4-12")
my_foods = ['pizza', 'falafel', 'carrot_cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
for item in my_foods:
    print(item)
print("My friend's favorite foods are:")
for item in friend_foods:
    print(item)

