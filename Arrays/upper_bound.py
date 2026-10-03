def upper_bound(arr, x):
    low = 0
    high = len(arr) - 1
    ans = len(arr)

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


arr = [1, 2, 4, 4, 4, 6, 8]
x = 4

print(upper_bound(arr, x))