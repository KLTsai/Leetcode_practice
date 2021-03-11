
if __name__ == '__main__':
    nums = [0,0]
    i = 0
    for idx,val in enumerate(nums):
        if(val != 0):
            nums[i] = val
            i+=1

    print(nums, i)
    while i< len(nums):
        if(nums[i] != 0):
            nums[i] = 0
        i+=1
    
    print(nums)