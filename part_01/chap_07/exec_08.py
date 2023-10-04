sandwich_orders = [
    "tuna", 'beaf', 'pork'
]
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)

print("\n")
sandwich_orders = [
    "tuna", 'beaf', 'pork', 'pastrami', 'pastrami', 'pastrami'
]
finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)

print('\n')
places = []
while True:
    place = input("If you could visit one place in the world, where would you go? ")
    places.append(place)
    is_continue = input('continue?(yes/no) ')
    if is_continue == 'no':
        break
print(places)
