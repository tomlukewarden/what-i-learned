# Algorithm to find the largest number in a list of numbers.

def find_largest(arr):
    # Check if the list is empty
    if not arr:
        return None  # Return None if the list is empty
    
    # Initialize the first element of the list as the largest
    largest = arr[0]
    
    # Loop through the rest of the list, starting from the second element
    for num in arr[1:]:
        # Compare each element with the current largest number
        if num > largest:
            largest = num  # If the current number is greater, update the largest
    
    # Return the largest number found
    return largest

# Test the find_largest function with an example list
arr = [23, 12, 55, 78, 34, 2, 9]
print("The largest number in the list is:", find_largest(arr))
