def maxsubarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

def max(a, b):
    return a if a > b else b

def main():
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxsubarray(arr))

if __name__ == "__main__":  
    main()