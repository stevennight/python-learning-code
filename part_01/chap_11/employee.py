class Employee:
    def __init__(self, first_name, second_name, salary):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount
