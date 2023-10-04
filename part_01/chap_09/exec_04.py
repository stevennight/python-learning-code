class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"name: {self.restaurant_name}")
        print(f'type: {self.cuisine_type}')

    def open_restaurant(self):
        print(f'restaurant {self.restaurant_name.title()} is open!')

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


a_restaurant = Restaurant('KK', 'bing')
print(a_restaurant.restaurant_name)
print(a_restaurant.cuisine_type)
print(a_restaurant.number_served)
a_restaurant.number_served = 100
print(a_restaurant.number_served)
a_restaurant.set_number_served(200)
print(a_restaurant.number_served)
a_restaurant.increment_number_served(1)
print(a_restaurant.number_served)


class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(
            f"Name: {self.first_name.title()} {self.last_name.title()},"
            f" age: {self.age}, location: {self.location}"
        )

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


guest1 = User("Fana", "Go", 10, 'Guangzhou')
guest1.describe_user()
guest1.greet_user()
guest1.increment_login_attempts()
guest1.increment_login_attempts()
guest1.increment_login_attempts()
print(guest1.login_attempts)
guest1.reset_login_attempts()
print(guest1.login_attempts)
