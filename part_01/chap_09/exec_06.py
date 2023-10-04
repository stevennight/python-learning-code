from exec_04 import Restaurant
from exec_04 import User


class IceCreateStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = [
            '草莓', '橙子', '榴莲'
        ]

    def show_flavors(self):
        print(self.flavors)


ice_cream_stand = IceCreateStand("Bing Ice Cream", 'cream')
ice_cream_stand.show_flavors()


class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges([
            'can add post', 'can delete post', 'can ban user'
        ])


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privilege(self):
        print(self.privileges)


admin_user = Admin('admin', 'admin', 99, 'Hangzhou')
admin_user.privileges.show_privilege()


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def get_range(self):
        range = 0
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        self.battery_size = 100


class ElectricCar:
    def __init__(self):
        self.battery = Battery()


car = ElectricCar()
car.battery.get_range()
car.battery.upgrade_battery()
car.battery.get_range()



