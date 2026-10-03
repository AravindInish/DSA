def sort_012(arr):
    low=0
    mid=0
    high=len(arr)-1

    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1

    return arr

def main():
    arr=[0,1,2,0,1,2]
    print(sort_012(arr))

if __name__=="__main__":
    main()