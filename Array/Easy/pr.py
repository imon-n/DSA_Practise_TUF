# nums = [-1,-100,3,99]
# k = 2

# nums = [1,2,3,4,5,6,7]
# k = 3

def solve(arr, n):
    temp = [0] * n
    print(temp)
    for i in range(1, n):
        temp[i - 1] = arr[i]
    temp[n - 1] = arr[0]

    for i in range(n):
        print(temp[i], end=" ")
    print()

n = 3
arr = [1, 2, 3, 4, 5, 6, 7]
solve(arr, n)





# new_nums = []

# start_index = len(nums) - k;

# for i in range(start_index,len(nums)):
#     new_nums.append(nums[i])

# for i in range(0,start_index):
#     new_nums.append(nums[i])

# print(new_nums)