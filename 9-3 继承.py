import electric_car

my_tesla = electric_car.ElectricCar('Tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery_size()
my_tesla.fill_gas_tank()
my_tesla.battery_size.describe_battery()

my_benz = electric_car.Car("benz", "E300L", 2020)
my_benz.fill_gas_tank()
