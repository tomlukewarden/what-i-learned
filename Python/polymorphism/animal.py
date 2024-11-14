# Define a base class called Animal
class Animal:
    # Method that will be overridden by subclasses
    def speak(self):
        pass  # Placeholder method, no specific behavior in the base class

# Define a Dog class that inherits from Animal
class Dog(Animal):
    # Override the speak method for Dog
    def speak(self):
        return "Woof! Woof!"

# Define a Cat class that inherits from Animal
class Cat(Animal):
    # Override the speak method for Cat
    def speak(self):
        return "Meow!"

# Function to demonstrate polymorphism
# - This function takes an Animal and calls its speak method
def make_animal_speak(animal):
    print(animal.speak())

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Use the make_animal_speak function with different Animal subclasses
make_animal_speak(dog)  # Outputs: Woof! Woof!
make_animal_speak(cat)  # Outputs: Meow!

# Explanation of polymorphism:
# - Both Dog and Cat are subclasses of Animal and implement the same method, `speak`, in their own way.
# - The function `make_animal_speak` can take any object that has a `speak` method (any Animal subclass).
# - This demonstrates polymorphism because Dog and Cat can be used interchangeably as "Animal" types, 
#   and they respond differently to the same `speak` method call.
