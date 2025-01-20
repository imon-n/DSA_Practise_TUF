nums = [1,0,1,1,0,1]
cnt = 0
temp = []

if nums[len(nums)-1] == 1:
    nums.append(0)

for i in nums:
    if i == 1:
        cnt = cnt + 1
    else:
        temp.append(cnt)
        cnt = 0

print(max(temp))