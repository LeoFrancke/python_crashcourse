# exercise 9.3

class User:
    """ description """

    def __init__(self, first_name, last_name, age, location):
        self.id_user = len(first_name + last_name)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location


    def describe_user(self):
        """Summary of user info."""
        print(f"The user {self.first_name} {self.last_name} is {self.age}yo and lives in {self.location}.")

    def greet_user(self):
        """Personalized greeting to user."""
        print(f"Welcome, {self.first_name} {self.last_name}!")


user_1 = User('leo', 'francke', '999', 'Campinas')
user_2 = User('test', 'surname', '777', 'Ottawa')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

