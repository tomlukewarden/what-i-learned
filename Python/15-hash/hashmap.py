# Creating a hash map (dictionary)
hash_map = {}

# Adding key-value pairs
hash_map["name"] = "Alice"
hash_map["age"] = 25
hash_map["city"] = "New York"

# Accessing values
print(hash_map["name"])  # Output: Alice
print(hash_map["age"])   # Output: 25

# Modifying values
hash_map["age"] = 26

# Removing key-value pairs
del hash_map["city"]

# Checking for keys
if "name" in hash_map:
    print("Name is in the hash map")