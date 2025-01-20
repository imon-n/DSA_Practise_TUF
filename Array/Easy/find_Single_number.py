nums = [1,2,2,1,4,7,7,4,0]

nums.sort()

if len(nums) == 1:
    index = nums[0]
elif nums[len(nums)-1] != nums[len(nums)-2]:
    index = nums[len(nums)-1]
else:
    for i in range(1,len(nums)):
        if nums[0] != nums[1]:
            index = nums[0]
            break
        elif nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
            index = nums[i]
            break

print(index)