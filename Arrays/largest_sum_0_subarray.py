class solution:
    def largest_sum_0_subarray(arr):
        prefix_sum=0
        max_length=0
        first_index={}

        for i in range(len(arr)):
            prefix_sum+=arr[i]

            if prefix_sum==0:
                max_length=i+1
            elif prefix_sum in first_index:
                max_length=max(max_length,i-first_index[prefix_sum])
            else:
                first_index[prefix_sum]=i

        return max_length

sol=solution()
arr=[15,-2,2,-8,1,7,10,23]
print("Length of the largest subarray with sum 0:", sol.largest_sum_0_subarray(arr))