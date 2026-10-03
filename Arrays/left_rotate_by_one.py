def left_rotate_by_one(arr):
  
    if not arr:
        return arr  # Return the empty array as is
    
    first_element = arr[0]  # Store the first element
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]  # Shift elements to the left
    arr[-1] = first_element  # Place the first element at the end
    
    return arr 

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]

    print("Original Array:", data)

    rotated_array = left_rotate_by_one(data)

    print("Array after Left Rotation by One:", rotated_array)