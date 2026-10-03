class solution:
    def binary_search(self,arr,x):
        low=0
        high=len(arr)-1
        while low<=high:
            mid=low+(high-low)//2
            if arr[mid]==x:
                return mid
            elif arr[mid]<x:
                low=mid+1
            else:
                high=mid-1
        return -1


sol=solution()
arr=[1,2,3,4,5,6,7,8,9]
print("The element 5 is at index:", sol.binary_search(arr,5))