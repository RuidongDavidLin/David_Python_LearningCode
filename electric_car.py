class Car:
    """一次模拟汽车的简答尝试。"""
    def __init__(self, make, model, year):
         self.make = make
         self.model = model
         self.year = year
         self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        elif mileage < self.odometer_reading:
            print("Warning: You can't roll back thr mileage.")
        return mileage
    
    def increade_odometer(self, mileage):
        if mileage >= 0:
            self.odometer_reading += mileage
        elif mileage < 0:
            print("Warning: You can't roll back the odometer.")
        return mileage
    
    def fill_gas_tank(self):
        print("This car's gas tank has been filled.")
        
        
class Battery:
    """一次模拟电动汽车电瓶的简单尝试"""
    
    def __init__(self, battery_size = 75):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """打印一条显示电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-KWh battery.")
        
# class ElectricCar(Car):
#     """电动汽车的独到之处。"""
    
#     def __init__(self, make, model, year):
#         """初始化父类的属性"""
#         super().__init__(make, model, year)

# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         """
#         初始化父类的属性。
#         再初始化电动汽车特有的属性。
#         """
#         super().__init__(make, model, year)
#         self.battery_size = 75
    
#     def describe_battery(self):
#         """打印一条描述电瓶容量的消息。"""
#         print(f"This car has a {self.battery_size}-KWh battery.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = Battery(65)
        
    def describe_battery_size(self):
        print(f"The battery_size is {self.battery_size.battery_size}-KWh.")
    
    def fill_gas_tank(self):
        print("This car is an electtric car which does't have a gas tank!")