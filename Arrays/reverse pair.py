class Solution:

    def merge(self, arr, low, mid, high):
        count = 0
        j = mid + 1

        # Count reverse pairs
        for i in range(low, mid + 1):
            while j <= high and arr[i] > 2 * arr[j]:
                j += 1

            count += j - (mid + 1)

        # Normal merge
        temp = []
        i = low
        j = mid + 1

        while i <= mid and j <= high:

            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1

        while j <= high:
            temp.append(arr[j])
            j += 1

        # Copy back
        for k in range(len(temp)):
            arr[low + k] = temp[k]

        return count

    def mergeSort(self, arr, low, high):

        count = 0

        if low < high:
            mid = (low + high) // 2

            count += self.mergeSort(arr, low, mid)
            count += self.mergeSort(arr, mid + 1, high)

            count += self.merge(arr, low, mid, high)

        return count

    def reversePairs(self, arr):
        return self.mergeSort(arr, 0, len(arr) - 1)


# Example
arr = [1, 3, 2, 3, 1]

obj = Solution()

print("Number of Reverse Pairs:", obj.reversePairs(arr))