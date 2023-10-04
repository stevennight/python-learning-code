from restaurant import Restaurant

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