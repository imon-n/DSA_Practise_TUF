class Solution:
    def merge(self, arr, l, m, r):
        left = arr[l:m+1]  # Left half
        right = arr[m+1:r+1]  # Right half

        i, j, k = 0, 0, l

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    # Recursive function to divide and sort
    def mergeSort(self, arr, l, r):
        if l < r:
            m = (l + r) // 2
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self.merge(arr, l, m, r)
