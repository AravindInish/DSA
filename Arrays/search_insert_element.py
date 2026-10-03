class solution:
    def searchinsert(self, arr, target):
       low=0
       high=len(arr)-1

       while low<=high:
           mid=low+(high-low)//2

           if arr[mid]==target:
               return mid
           elif arr[mid]<target:
               low=mid+1
           else:
               high=mid-1

           return low 

sol=solution()

arr=[1,3,5,6]
target=5

print("Target found at index:", sol.searchinsert(arr, target))