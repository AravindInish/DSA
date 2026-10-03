class solution:
    def floor(self, arr, target):
        low=0
        high=len(arr)-1
        floor_index=-1

        while low<=high:
            mid=low+(high-low)//2

            if arr[mid]==target:
                return mid
            elif arr[mid]<target:
                floor_index=mid
                low=mid+1
            else:
                high=mid-1

        return floor_index

    def ceil(self, arr, target):
        low=0
        high=len(arr)-1
        ceil_index=-1

        while low<=high:
            mid=low+(high-low)//2

            if arr[mid]==target:
                return mid
            elif arr[mid]<target:
                low=mid+1
            else:
                ceil_index=mid
                high=mid-1

        return ceil_index

    def main(self):
        arr=[1,2,4,6,8]
        target=5

        floor_index=self.floor(arr,target)
        ceil_index=self.ceil(arr,target)

        print("Floor index:",floor_index)
        print("Ceil index:",ceil_index)

sol=solution()
sol.main()