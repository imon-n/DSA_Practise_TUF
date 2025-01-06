def bubble_sort(arr, n):
    if n == 1:
        return
    
    didSwap = 0

    for j in range(n-1): # j <= n-2 in c++
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1],arr[j]
            didSwap = 1

    if didSwap == 0:
        return
    
    bubble_sort(arr, n-1)

if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    n = len(arr)
    print(arr)
    bubble_sort(arr, n)
    print(arr)
