def bubble_sort(arr):
    """
    Sorts the input array using Bubble Sort algorithm.

    Parameters:
    arr (list): The unsorted list of integers.

    Returns:
    list: The sorted list of integers.
    """
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place, no need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

unsorted_array = [5, 2, 9, 1, 5, 6]
print("Unsorted Array:", unsorted_array)
bubble_sort(unsorted_array)
print("Sorted Array:", unsorted_array)


