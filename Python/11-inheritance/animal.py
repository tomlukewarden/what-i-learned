# Define a base class called Animal
# - This class represents general characteristics and behaviors of an animal
class Animal:
    # Constructor method to initialize the name attribute for an Animal instance
    def __init__(self, name):
        self.name = name  # Each Animal instance will have a name attribute
    
    # Method to simulate the sound an animal makes
    def make_sound(self):
        print("Some generic animal sound")

# Define a derived class called Dog that inherits from the Animal class
# - This class represents a specific type of animal, so it inherits properties and behaviors from Animal
class Dog(Animal):
    # Constructor method to initialize a Dog instance
    # - We use super() to call the constructor of the parent (Animal) class to set the name attribute
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class's constructor to initialize the name
        self.breed = breed  # Dog class has an additional attribute, breed
    
    # Override the make_sound method from the Animal class
    # - Dogs have a specific sound, so we customize it here
    def make_sound(self):
        print("Woof! Woof!")

    # New method specific to Dog
    def fetch(self):
        print(f"{self.name} is fetching the ball")

# Create an instance of Animal
generic_animal = Animal("Generic Animal")
generic_animal.make_sound()  # Outputs: Some generic animal sound

# Create an instance of Dog
dog = Dog("Buddy", "Golden Retriever")
dog.make_sound()  # Outputs: Woof! Woof! (specific to Dog class)
dog.fetch()       # Outputs: Buddy is fetching the ball

# Explanation of inheritance:
# - Inheritance allows a new class (Dog) to use the methods and properties of an existing class (Animal).
# - The Dog class inherits the `name` attribute and the `make_sound` method from Animal.
# - We can also override methods in the derived class, like `make_sound`, to provide behavior specific to Dog.
# - Additionally, the Dog class can have its own unique methods (like fetch) and attributes (like breed),
#   making it more specialized than the general Animal class.
