def recursive_insertion_sort(arr, n=None):
    if n is None:
        n = len(arr)

    if n <= 1:
        return arr

    recursive_insertion_sort(arr, n - 1)

    last = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = last

    return arr


if __name__ == "__main__":
    data = [4, 6, 2, 5, 7, 9, 1, 3]

    print("Original Array:", data)

    sorted_arr = recursive_insertion_sort(data)

    print("Sorted Array using Recursive Insertion Sort:", sorted_arr)