class solution:
    def count_subarray(arr,k):
        prefix_sum=0
        count=0
        prefix_sum_count={}

        for i in range(len(arr)):
            prefix_sum+=arr[i]

            if prefix_sum==k:
                count+=1

            if (prefix_sum-k) in prefix_sum_count:
                count+=prefix_sum_count[prefix_sum-k]

            if prefix_sum in prefix_sum_count:
                prefix_sum_count[prefix_sum]+=1
            else:
                prefix_sum_count[prefix_sum]=1

        return count

sol=solution()
arr=[10,2,-2,-20,10]
k=-10 
print("Count of subarrays with sum", k, ":", sol.count_subarray(arr,k))