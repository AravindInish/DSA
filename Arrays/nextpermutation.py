def nextPermutation(nums):
    n = len(nums)

    # Step 1: Find the pivot
    i = n - 2

    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # Step 2: Find the least greater element
    # than the pivot and swap
    if i >= 0:
        j = n - 1

        while nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]

    # Step 3: Reverse the elements after pivot
    left = i + 1
    right = n - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def main():
    nums = [1, 2, 3]
    print("Original array:", nums)
    nextPermutation(nums)
    print("Next permutation:", nums)

if __name__ == "__main__":
    main()


