# Define a class called Car
# - A class is a blueprint for creating objects, defining properties (attributes) and behaviors (methods)
class Car:
    # Constructor method to initialize attributes when a Car object is created
    def __init__(self, make, model, year):
        # Attributes to store car's make, model, and year
        # - self.make, self.model, and self.year are instance variables
        self.make = make  # e.g., "Toyota"
        self.model = model  # e.g., "Corolla"
        self.year = year  # e.g., 2020
    
    # Method to describe the car
    # - A method is a function defined inside a class that operates on its instances
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

    # Method to start the car
    def start(self):
        print(f"The {self.make} {self.model} is starting.")

# Creating instances (objects) of the Car class
# - Each instance represents a unique car with specific make, model, and year
car1 = Car("Toyota", "Corolla", 2020)  # Creates a Toyota Corolla car
car2 = Car("Honda", "Civic", 2018)     # Creates a Honda Civic car

# Using methods to interact with car1 and car2
car1.display_info()  # Outputs: 2020 Toyota Corolla
car1.start()         # Outputs: The Toyota Corolla is starting.

car2.display_info()  # Outputs: 2018 Honda Civic
car2.start()         # Outputs: The Honda Civic is starting.

# Explanation of basic class concepts:
# - The Car class defines a blueprint for creating car objects with attributes like make, model, and year.
# - The `__init__` method is a special method (constructor) that initializes attributes when an instance is created.
# - Methods like display_info and start allow instances to perform actions and access their own data.
# - Each car created (car1 and car2) is a separate instance of the Car class with its own data.
