class solution:
    def find_missing_and_repeating(self, arr):
        n = len(arr)

        xor=0

        for num in arr:
            xor^=num

        for i in range(1,n+1):
            xor^=i

        bit=xor & -xor

        x=0
        y=0

        for num in arr:
            if num & bit:
                x^=num
            else:
                y^=num

        for i in range(1,n+1):
            if i & bit:
                x^=i
            else:
                y^=i

        if arr.count(x) == 2:
            return [x, y]        
        else:
            return [y, x]


sol=solution()
arr=[4, 3, 6, 2, 1, 1]
result=sol.find_missing_and_repeating(arr)
print("Missing and Repeating elements:", result)
    