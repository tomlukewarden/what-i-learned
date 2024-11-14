# Bubble Sort Algorithm: A simple sorting algorithm that repeatedly steps through
# the list, compares adjacent elements, and swaps them if they are in the wrong order.
# The pass through the list is repeated until the list is sorted.

def bubble_sort(arr):
    # 'n' is the length of the array
    n = len(arr)
    
    # Outer loop: We need to make several passes over the list
    for i in range(n):
        # A flag to detect if a swap was made in this pass
        swapped = False
        
        # Inner loop: Iterate through the list, comparing adjacent elements
        for j in range(0, n-i-1):  # The last i elements are already sorted
            # Compare the adjacent elements
            if arr[j] > arr[j+1]:
                # If the current element is greater than the next one, swap them
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True  # Mark that a swap was made

        # If no swaps were made during this pass, the list is already sorted
        if not swapped:
            break  # Exit the loop early, as no further passes are needed

    return arr  # Return the sorted list

# Test the bubble_sort function with an example list
arr = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", arr)

sorted_arr = bubble_sort(arr)  # Call the bubble_sort function
print("Sorted array:", sorted_arr)
