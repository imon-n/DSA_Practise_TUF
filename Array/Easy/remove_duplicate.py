def removeDuplicates(nums):
    if not nums: 
        return 0
    
    index = 1  
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]: 
            nums[index] = nums[i] 
            index += 1
    
    return index  


if __name__ == "__main__":
    nums = [0, 0,1, 1, 2, 2, 3, 3, 4]
    new_length = removeDuplicates(nums) 
    print(f"New length: {new_length}")
    print(f"Array with unique elements: {nums[:new_length]}")
