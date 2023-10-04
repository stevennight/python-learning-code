friends = ['ma', 'zhao', 'liang']
print(f"Welcome to my diner, {friends[0].title()}")
print(f"Welcome to my diner, {friends[1].title()}")
print(f"Welcome to my diner, {friends[2].title()}")

print(f"3 {friends[2].title()} Not Come.")
friends[2] = "zhi"
print(f"Welcome to my diner, {friends[0].title()}")
print(f"Welcome to my diner, {friends[1].title()}")
print(f"Welcome to my diner, {friends[2].title()}")

print("I found a bigger table")
friends.insert(0, "zi")
friends.insert(2, "wu")
friends.append("guo")
print(f"Welcome to my diner, {friends[0].title()}")
print(f"Welcome to my diner, {friends[1].title()}")
print(f"Welcome to my diner, {friends[2].title()}")
print(f"Welcome to my diner, {friends[3].title()}")
print(f"Welcome to my diner, {friends[4].title()}")
print(f"Welcome to my diner, {friends[5].title()}")


print("Only two friend could comes")
friends.pop()
friends.pop(2)
friends.remove('zhi')
friends.pop()
print(f"Welcome to my diner, {friends[0].title()}")
print(f"Welcome to my diner, {friends[1].title()}")
del friends[0]
del friends[0]
print(friends)
