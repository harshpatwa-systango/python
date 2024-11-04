class Car:
    total_car = 0

    def __init__(self, brand, model):
        # Private attributes for brand and model
        self.__brand = brand
        self.__model = model
        Car.total_car += 1  

    # Method to get the brand with a specific format
    def get_brand(self):
        return self.__brand + " !"
    
    # String representation of the Car object
    def __str__(self):
        return f"{self.brand} {self.model}"

    # Method to get the full name of the car (brand and model)
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    # Method to describe the fuel type
    def fuel_type(self):
        return "Petrol or Diesel"
    
    # Static method that provides a general description of cars
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    # Property for the model attribute
    @property
    def model(self):
        return self.__model
    
    # Setter for the model attribute
    @model.setter
    def model(self, value):
        self.__model = value

    # Property for the brand attribute
    @property
    def brand(self):
        return self.__brand


# ElectricCar is a subclass of Car
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        # Initialize the parent Car class
        super().__init__(brand, model)
        self.battery_size = battery_size  

    # Overriding the fuel_type method for electric cars
    def fuel_type(self):
        return "Electric charge"


# Creating an instance of ElectricCar
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# Checking if my_tesla is an instance of Car or ElectricCar
print(isinstance(my_tesla, Car))        
print(isinstance(my_tesla, ElectricCar)) 

# Getting the brand and fuel type of my_tesla
print(my_tesla.get_brand())  
print(my_tesla.fuel_type())   

# Creating an instance of Car
my_car = Car("Tata", "Safari")
my_car.model = "City"  # Changing the model using the setter

# Getting the general description of cars
print(my_car.general_description()) 
print(my_car.model) 

# Creating another instance of Car
my_car = Car("Toyota", "Corolla")
print(my_car.brand)   
print(my_car.model)  
print(my_car)        
print(my_car.full_name()) 
# Creating another instance of Car to demonstrate property access
my_new_car = Car("Tata", "Safari")
print(my_new_car.model) 
