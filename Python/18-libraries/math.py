# Importing the math module
import math

# ---------------------------------------------------
# Example 1: Using math.sqrt() to calculate the square root
# ---------------------------------------------------
number = 16
square_root = math.sqrt(number)
print(f"The square root of {number} is {square_root}")  # Output: 4.0

# ---------------------------------------------------
# Example 2: Using math.pow() to calculate power
# ---------------------------------------------------
base = 2
exponent = 3
power_result = math.pow(base, exponent)
print(f"{base} raised to the power of {exponent} is {power_result}")  # Output: 8.0

# ---------------------------------------------------
# Example 3: Using math.factorial() to find factorial
# ---------------------------------------------------
factorial_num = 5
factorial_result = math.factorial(factorial_num)
print(f"The factorial of {factorial_num} is {factorial_result}")  # Output: 120

# ---------------------------------------------------
# Example 4: Using math.pi to get the value of pi
# ---------------------------------------------------
circle_radius = 7
circle_area = math.pi * (circle_radius ** 2)
print(f"The area of a circle with radius {circle_radius} is {circle_area:.2f}")  # Output: 153.94

# ---------------------------------------------------
# Example 5: Using math.radians() to convert degrees to radians
# ---------------------------------------------------
angle_in_degrees = 45
angle_in_radians = math.radians(angle_in_degrees)
print(f"{angle_in_degrees} degrees is equal to {angle_in_radians:.2f} radians")  # Output: 0.79

# ---------------------------------------------------
# Example 6: Using math.ceil() and math.floor() for rounding
# ---------------------------------------------------
float_number = 3.7
ceil_value = math.ceil(float_number)  # Round up
floor_value = math.floor(float_number)  # Round down

print(f"The ceiling of {float_number} is {ceil_value}")  # Output: 4
print(f"The floor of {float_number} is {floor_value}")  # Output: 3
