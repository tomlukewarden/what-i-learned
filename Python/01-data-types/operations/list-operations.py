# Example Python code showing various list operations

# Initialize a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ---------------------------------------------------
# 1. Accessing Elements by Indexing
# ---------------------------------------------------
# Access the first element (index 0)
print("First element:", my_list[0])  # Output: 1
# Access the last element (index -1)
print("Last element:", my_list[-1])  # Output: 10

# ---------------------------------------------------
# 2. Slicing a List
# ---------------------------------------------------
# Get a sublist from index 2 to 5 (excluding index 5)
sublist = my_list[2:5]
print("Sliced list (from index 2 to 5):", sublist)  # Output: [3, 4, 5]

# Get a sublist from the beginning to index 3 (excluding index 3)
sublist = my_list[:3]
print("Sliced list (up to index 3):", sublist)  # Output: [1, 2, 3]

# Get a sublist from index 5 to the end
sublist = my_list[5:]
print("Sliced list (from index 5 to end):", sublist)  # Output: [6, 7, 8, 9, 10]

# ---------------------------------------------------
# 3. Step in Slicing
# ---------------------------------------------------
# Get every second element starting from index 0
sublist = my_list[::2]
print("Every second element:", sublist)  # Output: [1, 3, 5, 7, 9]

# ---------------------------------------------------
# 4. List Concatenation (Adding Lists Together)
# ---------------------------------------------------
# Concatenate two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("Concatenated list:", concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

# ---------------------------------------------------
# 5. List Repetition (Multiplying Lists)
# ---------------------------------------------------
# Repeat a list three times
repeated_list = [0] * 3
print("Repeated list:", repeated_list)  # Output: [0, 0, 0]

# ---------------------------------------------------
# 6. List Length
# ---------------------------------------------------
# Get the length of a list
list_length = len(my_list)
print("Length of the list:", list_length)  # Output: 10

# ---------------------------------------------------
# 7. Adding Elements to a List
# ---------------------------------------------------
# Add an element to the end of the list using append()
my_list.append(11)
print("List after append:", my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Add multiple elements to the end of the list using extend()
my_list.extend([12, 13])
print("List after extend:", my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Insert an element at a specific position using insert()
my_list.insert(5, 'new')
print("List after insert:", my_list)  # Output: [1, 2, 3, 4, 5, 'new', 6, 7, 8, 9, 10, 11, 12, 13]

# ---------------------------------------------------
# 8. Removing Elements from a List
# ---------------------------------------------------
# Remove an element by value using remove()
my_list.remove(6)  # Removes the first occurrence of 6
print("List after remove:", my_list)  # Output: [1, 2, 3, 4, 5, 'new', 7, 8, 9, 10, 11, 12, 13]

# Remove an element by index using pop()
removed_element = my_list.pop(2)  # Removes and returns the element at index 2
print("List after pop:", my_list)  # Output: [1, 2, 4, 5, 'new', 7, 8, 9, 10, 11, 12, 13]
print("Removed element:", removed_element)  # Output: 3

# ---------------------------------------------------
# 9. List Comprehension
# ---------------------------------------------------
# Create a new list with squares of all numbers in the original list
squares = [x**2 for x in my_list if isinstance(x, int)]  # Only square integers, not strings
print("Squares of numbers:", squares)  # Output: [1, 4, 16, 25, 49, 64, 81, 100, 121, 144, 169]

# ---------------------------------------------------
# 10. Sorting a List
# ---------------------------------------------------
# Sort the list in ascending order (in-place)
my_list.sort()  # This modifies the list itself
print("List after sort:", my_list)

# Sort the list in descending order
my_list.sort(reverse=True)
print("List after reverse sort:", my_list)

# ---------------------------------------------------
# 11. Reversing a List
# ---------------------------------------------------
# Reverse the list in-place
my_list.reverse()
print("List after reverse:", my_list)

# ---------------------------------------------------
# 12. Checking for an Element in the List
# ---------------------------------------------------
# Check if an element exists in the list
if 5 in my_list:
    print("5 is in the list.")
else:
    print("5 is not in the list.")

# ---------------------------------------------------
# 13. Copying a List
# ---------------------------------------------------
# Create a copy of the list
copied_list = my_list.copy()
print("Copied list:", copied_list)

# ---------------------------------------------------
# 14. Clearing a List
# ---------------------------------------------------
# Clear all elements in the list
my_list.clear()
print("List after clear:", my_list)  # Output: []

