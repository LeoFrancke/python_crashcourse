# Exercise 9.5 - Login Attempts

class User:
    """ description """

    def __init__(self, first_name, last_name, age, location):
        self.id_user = len(first_name + last_name)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0


    def describe_user(self):
        """Summary of user info."""
        print(f"The user {self.first_name} {self.last_name} is {self.age}yo and lives in {self.location}.")


    def greet_user(self):
        """Personalized greeting to user."""
        print(f"Welcome, {self.first_name} {self.last_name}!")


    def increment_login_attempts(self):
        """Increment attribute login_attempts."""
        self.login_attempts += 1
        print(f"The user {self.first_name} tried to log in.")


    def reset_login_attempts(self):
        """Increment attribute login_attempts."""
        self.login_attempts = 0


new_user = User("John", "Doe", 30, "Canada")
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()

print(f"{new_user.first_name} tried to log in {new_user.login_attempts} times.")
new_user.reset_login_attempts()

print(f"\nLogin attempts reseted. \n{new_user.first_name} tried to log in {new_user.login_attempts} times.")

