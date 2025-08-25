# Example Python code showing various dictionary operations

# Initialize a dictionary
my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'email': 'john@example.com'
}

# ---------------------------------------------------
# 1. Accessing Values by Keys
# ---------------------------------------------------
# Access a value by its key
print("Name:", my_dict['name'])  # Output: John

# Using the get() method to access a value
print("Age using get():", my_dict.get('age'))  # Output: 30

# Access a value using a key that might not exist, returns None if key is missing
print("Country using get():", my_dict.get('country'))  # Output: None

# ---------------------------------------------------
# 2. Adding or Updating Elements
# ---------------------------------------------------
# Add a new key-value pair to the dictionary
my_dict['occupation'] = 'Engineer'
print("Dictionary after adding occupation:", my_dict)

# Update an existing value using the key
my_dict['age'] = 31
print("Dictionary after updating age:", my_dict)

# ---------------------------------------------------
# 3. Removing Elements
# ---------------------------------------------------
# Remove a key-value pair using the pop() method, returns the removed value
removed_value = my_dict.pop('email')
print("Removed email:", removed_value)  # Output: john@example.com
print("Dictionary after pop:", my_dict)

# Remove a key-value pair using del
del my_dict['city']
print("Dictionary after del city:", my_dict)

# Remove all key-value pairs using clear()
my_dict.clear()
print("Dictionary after clear:", my_dict)  # Output: {}

# ---------------------------------------------------
# 4. Checking if a Key Exists
# ---------------------------------------------------
# Check if a key exists using 'in'
if 'name' in my_dict:
    print("Key 'name' exists in the dictionary.")
else:
    print("Key 'name' does not exist in the dictionary.")

# ---------------------------------------------------
# 5. Dictionary Length
# ---------------------------------------------------
# Get the number of key-value pairs in the dictionary
dict_length = len(my_dict)
print("Length of dictionary:", dict_length)  # Output: 0 (after clear)

# ---------------------------------------------------
# 6. Iterating Over Keys, Values, or Both
# ---------------------------------------------------
# Iterate over the keys of the dictionary
print("Keys in the dictionary:")
for key in my_dict:
    print(key)  # Prints each key

# Iterate over the values of the dictionary
print("Values in the dictionary:")
for value in my_dict.values():
    print(value)  # Prints each value

# Iterate over the key-value pairs of the dictionary
print("Key-Value pairs in the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")  # Prints each key-value pair

# ---------------------------------------------------
# 7. Copying a Dictionary
# ---------------------------------------------------
# Create a shallow copy of the dictionary using copy()
my_dict_copy = my_dict.copy()
print("Copy of the dictionary:", my_dict_copy)

# ---------------------------------------------------
# 8. Merging Dictionaries
# ---------------------------------------------------
# Merge two dictionaries using the update() method
new_dict = {'country': 'USA', 'gender': 'Male'}
my_dict.update(new_dict)
print("Dictionary after merging with new_dict:", my_dict)

# ---------------------------------------------------
# 9. Dictionary Comprehension
# ---------------------------------------------------
# Create a new dictionary with only keys that are numbers
num_dict = {key: value for key, value in my_dict.items() if isinstance(value, int)}
print("Dictionary with integer values:", num_dict)

# ---------------------------------------------------
# 10. Sorting a Dictionary by Keys or Values
# ---------------------------------------------------
# Sorting a dictionary by keys
sorted_dict_by_key = dict(sorted(my_dict.items()))
print("Dictionary sorted by keys:", sorted_dict_by_key)

# Sorting a dictionary by values
sorted_dict_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Dictionary sorted by values:", sorted_dict_by_value)

