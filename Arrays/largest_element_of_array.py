def find_largest_element(arr):
    if not arr:
        return None  # Return None for an empty array

    largest = arr[0]  # Assume the first element is the largest

    for num in arr:
        if num > largest:
            largest = num  # Update largest if a larger number is found

    return largest  # Return the largest element found

if __name__ == "__main__":
    data = [4, 6, 2, 5, 7, 9, 1, 3]

    print("Array:", data)

    largest_element = find_largest_element(data)

    print("Largest Element in the Array:", largest_element)