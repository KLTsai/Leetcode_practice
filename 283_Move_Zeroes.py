#要注意這題，以為測完testcase 可以AC
#有可能連續兩個0
#用append, pop, del 發生Wrong的機率很高

'''
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
'''
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