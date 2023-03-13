
def quicksort(arr):
    # This function implements quick sort algorithm
    if len(arr) <= 1:
        return arr  # Already sorted list with only one element

    # Select pivot element as middle index element 
    pivot = arr[len(arr) // 2]

    # Divide the arr into two sublists (left and right) smaller than and greater than pivot element respectively
    left_arr = [x for x in arr if x < pivot]
    middle_arr = [x for x in arr if x == pivot]
    right_arr = [x for x in arr if x > pivot]

    # Recursively apply quicksort to both sublists and concatenate the results
    return quicksort(left_arr) + middle_arr + quicksort(right_arr)


# Example usage of quicksort function
print(quicksort([3, 6, 8, 10, 1, 2, 1]))