n = 5
arr = [4, 1, 3, 9, 7]

for i in range(n-1,-1,-1):
    for j in range(1,n):
        if arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]

for i in arr:
    print(i,end=" ")