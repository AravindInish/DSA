def find_missinig_number(arr,n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    return missing_number

def sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 6, 7, 8]
    n = 8
    missing_number = find_missinig_number(arr, n)
    print(f"The missing number in the array is: {missing_number}")
    