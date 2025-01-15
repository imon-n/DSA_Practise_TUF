def rotate(nums,k):
    if not nums: 
        return 0
    
    new_nums = []

    start_index = len(nums) - k;
    

    for i in range(start_index,len(nums)):

# for i in range(start_index, end_index):
    

    
    return nums  


if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    rotate(nums,k) 
    for i in nums:
        print(i,end=" ")