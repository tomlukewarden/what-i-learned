import math

# Define a base class called Shape
class Shape:
    # Methods that will be overridden by subclasses
    def area(self):
        raise NotImplementedError("Subclass must implement area method")
    
    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter method")

# Define a Circle class that inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Unique attribute for Circle
    
    # Override area method for Circle
    def area(self):
        return math.pi * (self.radius ** 2)
    
    # Override perimeter method for Circle
    def perimeter(self):
        return 2 * math.pi * self.radius

# Define a Rectangle class that inherits from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width  # Width of the rectangle
        self.height = height  # Height of the rectangle
    
    # Override area method for Rectangle
    def area(self):
        return self.width * self.height
    
    # Override perimeter method for Rectangle
    def perimeter(self):
        return 2 * (self.width + self.height)

# Define a Triangle class that inherits from Shape
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        # Three sides of the triangle
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    # Override area method for Triangle (using Heron's formula)
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2  # Semi-perimeter
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    # Override perimeter method for Triangle
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Function to demonstrate polymorphism
# - This function takes a Shape and calls its area and perimeter methods
def display_shape_info(shape):
    print(f"Shape Info: {type(shape).__name__}")
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print("-" * 30)

# Create instances of each shape
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)
triangle = Triangle(side1=3, side2=4, side3=5)

# Use the display_shape_info function with different shapes
display_shape_info(circle)     # Outputs area and perimeter specific to Circle
display_shape_info(rectangle)  # Outputs area and perimeter specific to Rectangle
display_shape_info(triangle)   # Outputs area and perimeter specific to Triangle

# Explanation of polymorphism in this example:
# - Each shape subclass (`Circle`, `Rectangle`, `Triangle`) inherits from `Shape` and overrides `area` and `perimeter`.
# - The function `display_shape_info` can take any `Shape` object and call `area` and `perimeter` without knowing the exact shape type.
# - This allows us to treat each unique shape as a `Shape`, while each shape provides its own behavior for the same method calls.
