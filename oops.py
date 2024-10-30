class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"
    
    def __str__(self):
        return f"{self.brand} {self.model}"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def brand(self):
        return self.__brand


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


# Multi-level Inheritance
class SportsCar(ElectricCar):
    def __init__(self, brand, model, battery_size, max_speed):
        super().__init__(brand, model, battery_size)
        self.max_speed = max_speed

    def fuel_type(self):
        return f"{super().fuel_type()} with a sporty twist"


# Multiple Inheritance
class LuxuryFeatures:
    def __init__(self, luxury_level):
        self.luxury_level = luxury_level

    def luxury_description(self):
        return f"This car has a luxury level of: {self.luxury_level}"


class LuxuryCar(Car, LuxuryFeatures):
    def __init__(self, brand, model, luxury_level):
        Car.__init__(self, brand, model)
        LuxuryFeatures.__init__(self, luxury_level)

    def fuel_type(self):
        return "Premium petrol or diesel"


# Create instances
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
my_sports_car = SportsCar("Tesla", "Roadster", "100kWh", 250)
my_luxury_car = LuxuryCar("BMW", "7 Series", "High")

# single inheritance
print(isinstance(my_tesla, Car))  
print(isinstance(my_tesla, ElectricCar))  
print(my_tesla.get_brand())
print(my_tesla.fuel_type())

# multi-level inheritance
print(my_sports_car.full_name())
print(my_sports_car.fuel_type())
print(f"Max Speed: {my_sports_car.max_speed} km/h")

# multiple inheritance
print(my_luxury_car.full_name())
print(my_luxury_car.fuel_type())
print(my_luxury_car.luxury_description())

# property methods
my_car = Car("Tata", "Safari")
my_car.model = "City"
print(my_car.general_description())
print(my_car.model)

my_new_car = Car("Tata", "Safari")
print(my_new_car.model)
