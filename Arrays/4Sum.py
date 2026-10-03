def fourSum(nums, target):
    nums.sort()
    result = []

    n = len(nums)

    for i in range(n - 3):

        # Skip duplicate i
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):

            # Skip duplicate j
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:

                total = (
                    nums[i]
                    + nums[j]
                    + nums[left]
                    + nums[right]
                )

                if total == target:

                    result.append([
                        nums[i],
                        nums[j],
                        nums[left],
                        nums[right]
                    ])

                    left += 1
                    right -= 1

                    # Skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < target:
                    left += 1

                else:
                    right -= 1

    return result

def main():
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print("Input array:", nums)
    print("Target sum:", target)
    result = fourSum(nums, target)
    print("Unique quadruplets that sum to target:", result)

if __name__ == "__main__":
    main()