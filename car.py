class Car1:
    """一次模拟器汽车的简单尝试"""
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year 
    
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

# my_new_car = Car('audi', 'a4', '2019')
# print(my_new_car.get_descriptive_name())

class Car2:
    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.year = year
        self.make = make
        self.model = model
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.model} {self.make}"
        return long_name.title()
    def update_odometer(self, mileage):
        """
        将里程表读数设定为指定的值
        禁止将里程表的读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        elif mileage < self.odometer_reading:
            print("You can't roll back an odometer!")
        else:
            print("Warning:Error input!")
        return self.odometer_reading

class Car3:
    def __init__(self, year, model, make):
        self.year = year
        self.model = model
        self.make = make
        self.odometer = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.model} {self.make}"
        return long_name.title()
    
    def update_odom(self, odom):
        if odom >= self.odometer:
            self.odometer = odom
        elif odom < self.odometer:
            print("You can't roll back the odometer")
        return self.odometer
    
    def increase_odom(self, odom):
        if odom >= 0:
            self.odometer += odom
        elif odom < 0:
            print("You can't roll back the odometer")
        return self.odometer
    