def max_consecutive_ones(nums):
    max_streak = 0
    current_streak = 0
    for num in nums:
        if num == 1:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0

    return max_streak

def max(a, b):
    return a if a > b else b

def main():
    nums = [1, 1, 0, 1, 1, 1]
    result = max_consecutive_ones(nums)
    print(f"The maximum number of consecutive 1's is: {result}")

if __name__ == "__main__":
    main()