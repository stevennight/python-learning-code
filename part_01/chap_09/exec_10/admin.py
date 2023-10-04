from user import User

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