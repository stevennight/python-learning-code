class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"name: {self.restaurant_name}")
        print(f'type: {self.cuisine_type}')

    def open_restaurant(self):
        print(f'restaurant {self.restaurant_name.title()} is open!')


a_restaurant = Restaurant('KK', 'bing')
print(a_restaurant.restaurant_name)
print(a_restaurant.cuisine_type)
a_restaurant.describe_restaurant()
a_restaurant.open_restaurant()

first_restaurant = Restaurant('KK', 'bing')
second_restaurant = Restaurant('FF', 'google')
third_restaurant = Restaurant('CC', 'baidu')
first_restaurant.describe_restaurant()
second_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()


class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(
            f"Name: {self.first_name.title()} {self.last_name.title()},"
            f" age: {self.age}, location: {self.location}"
        )

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")


guest1 = User("Fana", "Go", 10, 'Guangzhou')
guest1.describe_user()
guest1.greet_user()
