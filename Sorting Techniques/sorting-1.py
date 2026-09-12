def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_idx=i
        for j in range(i+1,n):
            if(arr[j]<arr[min_idx]):
                min_idx=j
        if min_idx!=i:
            arr[i],arr[min_idx]=arr[min_idx],arr[i]

    return arr


def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break       

    return arr


def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
          key=arr[i]
          j=i-1
          while j>=0 and arr[j]>key:
                arr[j+1]=arr[j]
                j-=1
          arr[j+1]=key
    return arr       


if __name__=="__main__" :
    data=[13,46,24,52,20,9]
    print("Original Array :",data)
    ssorted_arr=selection_sort(data)
    print("Selection Sorted Array:",ssorted_arr)
    bsorted_arr=bubble_sort(data)
    print("Bubble Sorted Array:",bsorted_arr)
    isorted_arr=insertion_sort(data)
    print("Insertion Sorted Array:",isorted_arr)
