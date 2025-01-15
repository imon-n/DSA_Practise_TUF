class Solution(object):
    def moveZeroes(self, nums):
        new_nums = []
        cnt = 0

        for i in nums:
            if i != 0:
                new_nums.append(i)
            else:
                cnt += 1
        
        if len(new_nums) == 0:
            for i in nums:
                new_nums.append(0)
        else:
            for i in range(0,cnt):
                new_nums.append(0)
        
        for i in range(len(nums)):
            nums[i] = new_nums[i]