def findunion(arr1,arr2):
    i=0
    j=0
    union=[]

    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            union.append(arr1[i])
            i+=1
        elif arr1[i]>arr2[j]:
            union.append(arr2[j])
            j+=1
        else:
            union.append(arr1[i])
            i+=1
            j+=1

    # Append any remaining elements from either array
    while i < len(arr1):
        union.append(arr1[i])
        i += 1

    while j < len(arr2):
        union.append(arr2[j])
        j += 1

    return union


if __name__ == "__main__":
    arr1 = [1, 2, 4, 5, 6]
    arr2 = [2, 3, 5, 7]
    
    result = findunion(arr1, arr2)
    print("Union of the two sorted arrays:", result)