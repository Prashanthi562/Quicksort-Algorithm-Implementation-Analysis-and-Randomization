## Description:The process of choosing the pivot at a random place within the subarray increases the balance of the partitioning and ultimately the probability of avoiding the worst-case scenario time complexity since the start point is desirable.
import random

def randomized_quicksort(arr, low, high):
    # checking if the subarray has more than one element
    if low < high:
        # selecting a pivot from a random position
        pivot_index = random.randint(low, high)
        # moving the random pivot to the end
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        
        # dividing the array around the random pivot
        pi = partition(arr, low, high)

        # sorting the left side of the array
        randomized_quicksort(arr, low, pi - 1)
        # sorting the right side of the array
        randomized_quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    # choosing the pivot from the end
    pivot = arr[high]
    # starting the pointer for smaller values
    i = low - 1

    # going through the subarray from start to one before the end
    for j in range(low, high):
        # comparing the current element with the pivot
        if arr[j] <= pivot:
            # moving the pointer forward
            i += 1
            # swapping smaller element to the left side
            arr[i], arr[j] = arr[j], arr[i]

    # placing the pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # giving back the pivot position
    return i + 1

# creating a sample array for sorting
arr = [10, 7, 8, 9, 1, 5]
# showing the original array
print("Original array:", arr)
# running the randomized quicksort on the array
randomized_quicksort(arr, 0, len(arr) - 1)
# showing the sorted result
print("Sorted array (Randomized):", arr)
