class solution:
    def max_product(self, nums):
        current_max = nums[0]
        current_min = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]
            temp_max = max(x, current_max * x, current_min * x)
            temp_min = min(x, current_max * x, current_min * x)

            current_max = temp_max
            current_min = temp_min
            result = max(result, current_max)

        return result

sol = solution()
nums = [2, 3, -2, 4]
print("Maximum product subarray:", sol.max_product(nums))  # Output: 6