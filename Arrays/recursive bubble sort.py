def recursive_bubble_sort(arr,n=None):
    if n is None:
        n=len(arr)
    if n==1:
        return

    SWAPPED=False

    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            SWAPPED=True

    if not SWAPPED:
        return

    recursive_bubble_sort(arr, n - 1)

if __name__=="__main__":
    data=[4,6,2,5,7,9,1,3]
    print("Original Array :",data)
    rbsorted_arr=recursive_bubble_sort(data)
    print("Sorted Array by using Recursive Bubble Sort:",rbsorted_arr)