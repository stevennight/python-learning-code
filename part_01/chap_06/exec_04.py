dictionaries = {
    "key": "a name for a value in dict",
    "int": "a integer number",
    "string": "a text",
    "list": "a **** list",
    "defined": "check a variable is set?",
}
for key, value in dictionaries.items():
    print(f"{key}:\n\t{value}")

print('\n#6-05:')
rivers = {
    'nile': 'egypt',
    'huang river': 'china',
    'chang river': 'china',
}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print('#6-05(02)')
for river in rivers.keys():
    print(river.title())
print('#6-05(03)')
for country in rivers.values():
    print(country.title())
print('#6-05(04)')
for country in set(rivers.values()):
    print(country.title())

print('\n#6-06')
favorite_languages = {
    "bob": "java",
    "kate": "golang",
    "billy": "javascript"
}
members = [
    "bob", "kate", "filly", "cola", "sprite"
]
for member in members:
    if favorite_languages.get(member):
        print(f"Thank you, {member.title()}")
    else:
        print(f"Welcome to survey, {member.title()}")

