# Exercise 9.4: Number served

class Restaurant:
    """Model a simple restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type."""
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    
    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"The {self.name} is a {self.cuisine} restaurant.")


    def open_restaurant(self):
        """Print a msg indicating that it's open."""
        print(f"The {self.name} is open!")


    def set_number_served(self, number_served):
        """Set the number of clients served."""
        self.number_served = number_served


    def increment_number_served(self, increment):
        """Set the number of clients served."""
        self.number_served += increment


restaurant = Restaurant('X Burger', 'fast food')
print(f"So far the restaurant {restaurant.name} has served {restaurant.number_served} clients.")
restaurant.number_served = 3
print(f"So far the restaurant {restaurant.name} has served {restaurant.number_served} clients.")
restaurant.set_number_served(27)
print(f"So far the restaurant {restaurant.name} has served {restaurant.number_served} clients.")

restaurant.increment_number_served(48)
print(f"The number of clients served today was: {restaurant.number_served}.")

