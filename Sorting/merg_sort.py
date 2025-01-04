def merge(arr,low,mid,high):
    temp = []
    left = low # starting index of left half of arr
    right = mid+1 # starting index of right half of arr


    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # If elements on the left half are still left
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # If elements on the right half are still left
    while right <= high:
        temp.append(arr[right])
        right += 1


    for i in range(low, high + 1):
        arr[i] = temp[i - low] 
        print(arr[i],end=" ")   
    print(" ")  

def merge_sort(arr,low,high):
    if low >= high:
        return
    mid = (low+high)//2
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)

if __name__ == "__main__":
    arr = [9, 4, 7, 6, 3, 1, 5]
    n = len(arr)

    print("Before Sorting Array:")
    print(arr)
    merge_sort(arr, 0, n - 1)
    print("After Sorting Array:")
    print(arr)