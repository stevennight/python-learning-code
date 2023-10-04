people = [
    {
        "first_name": "Wang",
        "last_name": "Li"
    },
    {
        "first_name": "Wu",
        "last_name": "Juan"
    }
]
for person in people:
    print(person)


print("\n")
pets = [
    {
        "type": "dog",
        "master": "Wang Li",
    },
    {
        "type": "cat",
        "master": "Wu Juan",
    },
]
for pet in pets:
    print(pet)

print("\n")
favorite_places = {
    "WangLi": ["ShangHai", "BeiJing"],
    "WuJuan": ["GuangZhou", "GuiZhou"],
}
for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"{name.title()} Like Places Are:")
        for place in places:
            print(f"\t{place}")
    else:
        print(f"{name.title()} Like Place Is {places[0]}")

print("\n")
print("略")

print("\n")
cities = {
    "GuangZhou": {
        "country": "China",
        "population": 1_0000_0000,
        "fact": "Too Many People",
    },
    "GuiZhou": {
        "country": "China",
        "population": 800_0000,
        "fact": "Mountains",
    },
    "HaiNan": {
        "country": "China",
        "population": 500_0000,
        "fact": "Sea",
    },
}
for city_name, city_info in cities.items():
    print(f"{city_name}:")
    for key, value in city_info.items():
        print(f"\t{key}: {value}")

print('\n')
cities['ShangHai'] = {
    "country": "China",
    "population": 1_2000_0000,
    "fact": "East Bay",
}
print(cities)

print('\n')
for city_name, city_info in cities.items():
    city_info['fact'] = 'Change'
print(cities)
