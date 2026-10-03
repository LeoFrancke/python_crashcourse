# Exercise 9.2

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


restaurant_1 = Restaurant("Espeto de Prata", "churrascaria")
restaurant_2 = Restaurant("Brazil Burger", "Fast food")
restaurant_3 = Restaurant("Best Pizzaria", "Pizzaria")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

