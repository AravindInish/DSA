def two_sum(arr,k):
    seen={}
    for i,num in enumerate(arr):
        required=k-num
        if required in seen:
            return [seen[required],i]
        seen[num]=i

    return [-1,-1]

def main():
    arr=[2,7,11,15]
    k=18
    print(two_sum(arr,k))

if __name__=="__main__":
    main()