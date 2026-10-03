class solution:
    def lower_bound(self,arr,x):
        low=0
        high=len(arr)-1
        ans=-1
        while low<=high:
            mid=low+(high-low)//2
            if arr[mid]>=x:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

def main():
    sol=solution()
    arr=[1,2,3,4,5,6,7,8,9]
    print("The lower bound of 5 is at index:", sol.lower_bound(arr,5))
    print("The lower bound of 10 is at index:", sol.lower_bound(arr,10))
    print("The lower bound of 0 is at index:", sol.lower_bound(arr,0))

if __name__=="__main__":
    main()