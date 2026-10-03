arr=[16,17,4,3,5,2]

leaders=[]

max_right=arr[-1]

leaders.append(max_right)

for i in range(len(arr)-2,-1,-1):
    if(arr[i]>max_right):
        max_right=arr[i]
        leaders.append(max_right)

print("Leaders in the array are:", leaders[::-1])  