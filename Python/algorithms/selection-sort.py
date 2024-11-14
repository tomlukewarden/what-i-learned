# Selection Sort Algorithm: A simple sorting algorithm that repeatedly selects
# the smallest (or largest, depending on order) element from the unsorted portion
# of the list and swaps it with the first unsorted element.

def selection_sort(arr):
    # 'n' is the length of the array
    n = len(arr)
    
    # Outer loop: Iterate through the entire list
    for i in range(n):
        # Assume that the current index (i) holds the minimum value
        min_index = i
        
        # Inner loop: Find the smallest element in the remaining unsorted portion
        for j in range(i + 1, n):
            # If a smaller element is found, update min_index
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found smallest element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    # Return the sorted list
    return arr

# Test the selection_sort function with an example list
arr = [64, 25, 12, 22, 11]
print("Unsorted array:", arr)

sorted_arr = selection_sort(arr)  # Call the selection_sort function
print("Sorted array:", sorted_arr)
