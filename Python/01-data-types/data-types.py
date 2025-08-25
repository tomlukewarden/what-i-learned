# Integer - Represents whole numbers
x = 10
y = 3

# Perform basic arithmetic operations
sum_result = x + y  # Adding two integers
product_result = x * y  # Multiplying two integers

# Print results
print("Integer Operations:")
print(f"Sum: {sum_result}")
print(f"Product: {product_result}")
print("-" * 30)

# Float - Represents numbers with decimals
a = 10.5
b = 3.2

# Perform basic arithmetic operations with floats
division_result = a / b  # Dividing two floats
subtraction_result = a - b  # Subtracting two floats

# Print results
print("Float Operations:")
print(f"Division: {division_result:.2f}")  # Formatting the result to two decimal places
print(f"Subtraction: {subtraction_result:.2f}")
print("-" * 30)

# String - Represents a sequence of characters
name = "Alice"
greeting = "Hello"

# String concatenation (joining strings)
full_greeting = greeting + " " + name

# Print results
print("String Operations:")
print(f"Greeting: {full_greeting}")
print("-" * 30)

# List - Represents an ordered collection of items, which can be of different data types
my_list = [1, 2.5, "apple", True]

# Access elements from the list by index
first_element = my_list[0]  # First element (index 0)
last_element = my_list[-1]  # Last element (index -1)

# Add an element to the list
my_list.append("banana")

# Print results
print("List Operations:")
print(f"First Element: {first_element}")
print(f"Last Element: {last_element}")
print(f"Updated List: {my_list}")
print("-" * 30)

# Tuple - Represents an ordered, immutable collection of items
my_tuple = (10, 20, 30)

# Access elements from the tuple by index
tuple_element = my_tuple[1]  # Second element (index 1)

# Print results
print("Tuple Operations:")
print(f"Second Element of Tuple: {tuple_element}")
print("-" * 30)

# Dictionary - Represents a collection of key-value pairs
my_dict = {"name": "Alice", "age": 25, "city": "Wonderland"}

# Access value by key
name_value = my_dict["name"]

# Print results
print("Dictionary Operations:")
print(f"Name from Dictionary: {name_value}")
print(f"Full Dictionary: {my_dict}")
print("-" * 30)

# Boolean - Represents a value that is either True or False
is_adult = True
has_permission = False

# Print results
print("Boolean Operations:")
print(f"Is Adult: {is_adult}")
print(f"Has Permission: {has_permission}")
print("-" * 30)

# Explanation of data types:
# - **Integer**: Whole numbers. They can be used for arithmetic operations.
# - **Float**: Numbers with decimal points. They are useful for precision and can also be involved in arithmetic operations.
# - **String**: A sequence of characters used for text representation and manipulation.
# - **List**: A collection of ordered items, which can be modified (mutable). Lists can store elements of any data type.
# - **Tuple**: Similar to lists, but immutable (cannot be modified after creation). Useful for storing fixed collections of data.
# - **Dictionary**: A collection of key-value pairs, useful for associating data (e.g., a name with an age).
# - **Boolean**: A data type representing truth values. Can be either `True` or `False`.
