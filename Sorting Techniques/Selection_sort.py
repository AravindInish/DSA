def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n - 1):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first unsorted element
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
    return arr

# Example usage:
if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    print("Original array:", data)
    
    sorted_data = selection_sort(data)
    print("Sorted array:  ", sorted_data)
