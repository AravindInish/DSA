def linear_search(arr,tar):
    for i in range(len(arr)):
        if(arr[i]==tar):
            return i
    return -1

if __name__ == "__main__":
    arr=[90,52,64,25,78]
    result= linear_search(arr, 25)
    if result != -1:
        print("Element found at index:", result)
    else:
        print("Element not found in the array.")