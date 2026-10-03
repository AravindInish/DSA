class solution:
    def first_occurance(self,arr,target):
        low=0
        high=len(arr)-1
        first_index=-1

        while low<=high:
            mid=low+(high-low)//2

            if arr[mid]==target:
                first_index=mid
                high=mid-1
            elif arr[mid]<target:
                low=mid+1
            else:
                high=mid-1

        return first_index

    def last_occurance(self,arr,target):
        low=0
        high=len(arr)-1
        last_index=-1

        while low<=high:
            mid=low+(high-low)//2

            if arr[mid]==target:
                last_index=mid
                low=mid+1
            elif arr[mid]<target:
                low=mid+1
            else:
                high=mid-1

        return last_index

    def main(self):
        arr=[1,2,4,4,4,6,8]
        target=4

        first_index=self.first_occurance(arr,target)
        last_index=self.last_occurance(arr,target)

        print("First Occurance index:",first_index)
        print("Last Occurance index:",last_index)


sol=solution()
sol.main()