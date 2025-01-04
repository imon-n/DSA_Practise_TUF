N = 5
arr = [4, 1, 3, 9, 7]

for i in range(N-1):
    for j in range(i+1,N):
        if arr[i]>arr[j]:
            arr[i],arr[j] = arr[j],arr[i]

for i in arr:
    print(i,end=" ")