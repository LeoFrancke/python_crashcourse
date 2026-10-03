# Exercise 9.1: Restaurant

class Restaurant:
    """Model a simple restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type."""
        self.name = restaurant_name
        self.cuisine = cuisine_type

    
    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"The {self.name} is a {self.cuisine} restaurant.")


    def open_restaurant(self):
        """Print a msg indicating that it's open."""
        print(f"The {self.name} is open!")


restaurant = Restaurant("Espeto de Prata", "churrascaria")

restaurant.describe_restaurant()
restaurant.open_restaurant()

