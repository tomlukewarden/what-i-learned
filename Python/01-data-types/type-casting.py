# Example of type casting in Python

# Integer to Float (implicit or explicit)
x = 10  # Integer
x_float = float(x)  # Cast integer to float
print(f"Integer to Float: {x} -> {x_float}")

# Float to Integer (explicit)
y = 3.14  # Float
y_int = int(y)  # Cast float to integer (this truncates the decimal part)
print(f"Float to Integer: {y} -> {y_int}")

# String to Integer (explicit)
z = "42"  # String
z_int = int(z)  # Cast string to integer
print(f"String to Integer: {z} -> {z_int}")

# String to Float (explicit)
w = "3.14159"  # String
w_float = float(w)  # Cast string to float
print(f"String to Float: {w} -> {w_float}")

# Integer to String (explicit)
a = 100  # Integer
a_str = str(a)  # Cast integer to string
print(f"Integer to String: {a} -> {a_str}")

# List to String (explicit)
b = [1, 2, 3]  # List
b_str = str(b)  # Cast list to string (converts the list as a whole, not individual elements)
print(f"List to String: {b} -> {b_str}")

# String to Boolean (explicit)
c = "True"  # String
c_bool = bool(c)  # Cast string to boolean (non-empty string is True)
print(f"String to Boolean: {c} -> {c_bool}")

# Boolean to Integer (explicit)
d = True  # Boolean
d_int = int(d)  # Cast boolean to integer (True becomes 1, False becomes 0)
print(f"Boolean to Integer: {d} -> {d_int}")

# Boolean to String (explicit)
e = False  # Boolean
e_str = str(e)  # Cast boolean to string
print(f"Boolean to String: {e} -> {e_str}")

# List to Tuple (explicit)
f = [1, 2, 3]  # List
f_tuple = tuple(f)  # Cast list to tuple
print(f"List to Tuple: {f} -> {f_tuple}")

# Tuple to List (explicit)
g = (10, 20, 30)  # Tuple
g_list = list(g)  # Cast tuple to list
print(f"Tuple to List: {g} -> {g_list}")

# Explanation of Type Casting:
# - **int()**: Converts a float or string to an integer (decimal part is discarded).
# - **float()**: Converts an integer or string to a float (adds decimal point).
# - **str()**: Converts an integer, float, boolean, or other object to a string.
# - **bool()**: Converts a string, integer, or other object to a boolean (empty values become False).
# - **tuple()**: Converts a list or other iterable to a tuple (immutable version).
# - **list()**: Converts a tuple or other iterable to a list (mutable version).
