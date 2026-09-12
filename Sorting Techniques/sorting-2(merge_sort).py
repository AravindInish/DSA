def merge(arr,low,mid,high):
        left=arr[low:mid+1]
        right=arr[mid+1:high+1]
        i=0 
        j=0
        k=low
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1

        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1


def merge_sort(arr, low, high):
        if low>=high:
            return 
        else:
            mid=(low+high)//2
            merge_sort(arr,low,mid)
            merge_sort(arr,mid+1,high)
            merge(arr,low,mid,high)

        return arr


if __name__=="__main__":
        data=[3,1,2,4,1,5,2,6,4]
        print("Original Array :",data)
        msorted_array=merge_sort(data, 0, len(data)-1)
        print("Merge Sorted Array:",msorted_array)