import car 

my_newcar = car.Car1('audi','a4', 2019)
print(my_newcar.get_descriptive_name())

my_newcar = car.Car2('audi', 'a5', 20)
odometer = my_newcar.update_odometer(20)
print(odometer)

odometer = my_newcar.update_odometer(10)
print(odometer)

my_newcar = car.Car3("audi", "A6", 2019)
odometer = my_newcar.update_odom(10)
print(odometer)
odometer = my_newcar.increase_odom(15)
print(odometer)
odometer = my_newcar.increase_odom(-1)
print(odometer)