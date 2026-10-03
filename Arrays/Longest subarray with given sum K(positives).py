def longest_sub_arr(arr,k):
    left=0
    current_sum=0
    max_length=0
    n=len(arr)

    for right in range(n):
        current_sum+=arr[right]

        while current_sum>k and left<=right:
            current_sum-=arr[left]
            left+=1

        if current_sum==k:
            max_length=max(max_length,right-left+1)

    return max_length

def max(a,b):
    if a>b:
        return a
    else:
        return b

def main():
    arr=[1,2,3,7,5]
    k=12
    print(longest_sub_arr(arr,k))

if __name__=="__main__":
    main()