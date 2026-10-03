def rearrange_elements_by_sign(arr):
    pos=[]
    neg=[]

    for i in arr:
        pos.append(i) if i>=0 else neg.append(i)
        neg.append(i) if i<0 else pos.append(i)

    result=[]

    for i in range(len(arr)):
        result.append(pos[i]) 
        result.append(neg[i])

    return result

def main():
    arr=[1,2,3,-4,-1,4]
    print("Rearranged array:", rearrange_elements_by_sign(arr))