from random import randint, choice

#
# class Die:
#     def __init__(self, sides=6):
#         self.sides = sides
#
#     def roll_die(self):
#         print(randint(1, self.sides))
#
#
# die = Die(20)
# for i in range(1, 11):
#     die.roll_die()


lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e']
big = [1, 2, 'a', 'e', 'e', 'c']
len_big = len(big)
i = 0
while True:
    i += 1
    my_ticket = []
    for _ in range(1, len_big + 1):
        my_ticket.append(choice(lists))

    print(my_ticket)

    if big == my_ticket:
        print(f'中大奖了，执行次数{i}')
        break
