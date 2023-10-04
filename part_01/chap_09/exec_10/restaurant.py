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