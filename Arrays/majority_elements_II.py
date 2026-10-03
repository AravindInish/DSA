def majority_elements_II(nums):
    candidate1=None
    candidate2=None
    count1=0    
    count2=0

    for num in nums:
        if candidate1==num:
            count1+=1
        elif candidate2==num:
            count2+=1
        elif count1==0:
            candidate1=num
            count1=1
        elif count2==0:
            candidate2=num
            count2=1
        else:
            count1-=1
            count2-=1

    result=[]

    if nums.count(candidate1) > len(nums)//3:
        result.append(candidate1)

    if nums.count(candidate2) > len(nums)//3:
        result.append(candidate2)

    return result 

def main():
    nums = [1, 2, 3, 1, 1, 2, 2]
    print("Input array:", nums)
    result = majority_elements_II(nums)
    print("Majority elements (more than n/3 times):", result)

if __name__ == "__main__":
    main()
