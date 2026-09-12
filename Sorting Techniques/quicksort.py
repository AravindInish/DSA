def partition(arr, low, high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1


def quick_sort(arr, low, high):
    if low<high:
        pivot=partition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)

    return arr

if __name__ =="__main__":
    data=[4,6,2,5,7,9,1,3]
    print("Original Array :",data)
    qsorted_array=quick_sort(data, 0, len(data)-1)
    print("Sorted Array:",qsorted_array)
