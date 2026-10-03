def find_second_largest_element(arr):
    if not arr or len(arr) < 2:
        return None  # Return None if the array is empty or has less than 2 elements

    largest = second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest if second_largest != float('-inf') else None


if __name__=="__main__":
    data = [4, 6, 2, 5, 7, 9, 1, 3]

    print("Array:", data)

    second_largest_element = find_second_largest_element(data)

    print("Second Largest Element in the Array:", second_largest_element)