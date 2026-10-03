def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

def main():
    nums = [3,2,2,3,2,4,5,6,1,1,1,1]
    print(majority_element(nums))

if __name__ == "__main__":  
    main()