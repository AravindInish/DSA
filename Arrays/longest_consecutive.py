class solution:
    def longest_consecutive(nums):
        num_set=set(nums)
        longest=0

        for num in num_set:
            if num-1 not in num_set:
                current_num=num
                count=1

                while current_num+1 in num_set:
                    current_num+=1
                    count+=1

                longest=max(longest,count)

        return longest
sol=solution()
nums=[100,4,200,1,3,2]
print("Longest consecutive sequence length:", sol.longest_consecutive(nums))  