# create Electric_Car class to learn Inheritance.

class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        """Print car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")


    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it tries to roll the odometer back."""
        if self.odometer_reading <= mileage:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")


    def fill_gas_tank(self):
        """Fill the gas tank."""
        print("Filling your tank... Your tank is now full!")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initiate atttributes specific to Electric Cars."""
        super().__init__(make, model, year)
        self.battery_size = 40


    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


    def fill_gas_tank(self):
        """Overriding a method from the parent class."""
        print("This car doesn't have a gas tank!")
    

old_car = Car('renault', 'sandero', 2007)
print(old_car.get_descriptive_name())
old_car.fill_gas_tank()

print()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
my_leaf.fill_gas_tank()

