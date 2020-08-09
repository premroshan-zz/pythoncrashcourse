import car

my_tesla = car.ElectricCar('test','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_beetle_car = car.Car('volkswage','beetle','2019')
print(my_beetle_car.get_descriptive_name())
