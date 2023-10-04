import json


def get_stored_user(filename):
    try:
        with open(filename) as f:
            username = json.load(f)
            return username
    except FileNotFoundError:
        return None


def get_new_username(filename):
    username = input('What is your name? ')
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    filename = 'username.json'
    username = get_stored_user(filename)
    if username:
        confirmed = input(f'{username} or not? ')
        if confirmed == "n":
            username = None

    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(filename)
        print(f"We'll remember you when you come back, {username}!")





greet_user()
