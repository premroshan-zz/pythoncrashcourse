class Car:
    """A simple attempt to represent a car"""

    def __init__(self,make,model,year):
        """Constructor for a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.year}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the cars mileage"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """Update the odometer reading"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant rollback the odometer reading")

    def increment_odometer(self,increment):
        """Add to the odometer reading"""
        self.odometer_reading += increment

class Battery():
    """class that describes the battery"""
    def __init__(self,battery_size=75):
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Describe the battery of the car"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """print details about range provided by the batter"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge")

class ElectricCar(Car):
    """Represents an electric car"""
    def __init__(self,make,model,year):
        """Initialize attributes of the parent class"""
        super().__init__(make,model,year)
        self.battery = Battery()


my_tesla = ElectricCar('test','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()