'''
Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.


Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
'''

def matrixReshape(nums, r, c):
    r_len = len(nums)
    c_len = len(nums[0])
    
    if (r_len*c_len) != (r*c):
        return nums
    
    output = []
    element = []
    count = 0
    
    for idx, val in enumerate(nums):
        for i, j in enumerate(val):
            if(count < c):
                element.append(j)
                count+=1

            if(count == c):   
                output.append(element)
                count = 0
                element = []
    
    return output



if __name__ == '__main__' :
    nums = [[1,2],
            [3,4],
            [5,6]]
    #nums = [[1,2,3,4,5,6]]
    r = 1
    c = 6

    print("foo" * 3)
    print(2**3)

    kkkk = matrixReshape(nums, r, c)