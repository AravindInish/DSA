def longest_subarray(arr,k):
    prefix_sum=0
    max_length=0
    first_occurrence={0: -1}

    for i in range(len(arr)):
        prefix_sum+=arr[i]

        if prefix_sum-k in first_occurrence:
            max_length=max(max_length,i-first_occurrence[prefix_sum-k])

        if prefix_sum not in first_occurrence:
            first_occurrence[prefix_sum]=i

    return max_length

def max(a,b):
    if a>b:
        return a
    else:
        return b

def main():
    arr=[10,5,2,7,1,9]
    k=15
    print(longest_subarray(arr,k))

if __name__=="__main__":    
    main()