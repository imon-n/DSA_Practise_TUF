def merge(arr,l,m,r):
    # create temporary array
    left = arr[l:m+1] # Left half
    right = arr[m+1:r+1]   # Right half

    i,j,k = 0, 0, l

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

def merge_sort(arr,l,r):
    if l >= r:
        return
    m = (l+r)//2
    merge_sort(arr,l,m)
    merge_sort(arr,m+1,r)
    merge(arr,l,m,r)

if __name__ == "__main__":
    arr = [9, 4, 7, 6, 3, 1, 5]
    n = len(arr)

    print("Before Sorting Array:")
    print(arr)
    merge_sort(arr, 0, n - 1)
    print("After Sorting Array:")
    print(arr)