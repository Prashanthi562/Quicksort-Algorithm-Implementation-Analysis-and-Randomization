## Description:Quicksort algorithm uses the last element as the pivot and uses Lomuto partition to rearrange an array in place. In every recursion level through the cycle, elements are constantly swapped and compared until the subarray is correctly sorted. The partitioning algorithm ensures that the elements below the pivot are placed before them, and those above this value in the next positions, creating smaller subarrays that are further descended.
def quicksort(arr, low, high):
    # checking if the subarray has more than one element
    if low < high:
        # dividing the array and getting the pivot index
        pivot_index = partition(arr, low, high)
        # sorting the left part of the array
        quicksort(arr, low, pivot_index - 1)
        # sorting the right part of the array
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    # choosing the pivot element from the end
    pivot = arr[high]
    # starting the pointer for smaller elements
    i = low - 1

    # going through the array from low to high minus one
    for j in range(low, high):
        # comparing current element with pivot
        if arr[j] <= pivot:
            # moving the pointer forward
            i += 1
            # swapping the smaller element to the left
            arr[i], arr[j] = arr[j], arr[i]

    # placing the pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # returning the index of the pivot
    return i + 1

# creating an array for testing
arr = [10, 7, 8, 9, 1, 5]
# showing the array before sorting
print("Original array:", arr)
# calling the quicksort function on the whole array
quicksort(arr, 0, len(arr) - 1)
# showing the sorted array
print("Sorted array (Deterministic):", arr)
