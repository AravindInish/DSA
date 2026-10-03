def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place key at its correct position
        arr[j + 1] = key

    return arr


# Example
arr = [12, 11, 13, 5, 6]

print("Before Sorting:", arr)

insertion_sort(arr)

print("After Sorting:", arr)