'''
Example 1:
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
---------------------------------------------------------
Example 2:
Input: c = 3
Output: false
---------------------------------------------------------
Example 3:
Input: c = 4
Output: true
---------------------------------------------------------
Example 4:
Input: c = 2
Output: true
---------------------------------------------------------
Example 5:
Input: c = 1
Output: true
'''

#此題應用167解法 two pointer
def judgeSquareSum(num):
    if num < 0:
        return False

    start = 0
    sqr_data = num**0.5 #sqart
    end = round(sqr_data)

    if pow(end, 2) < num: #define last element in list
        end+=1
    elif pow(end, 2) == num:
        return True

    element = range(start, end)
    data_sum = 0

    while start < end:
        data_sum = pow(element[start], 2) + pow(element[end-1], 2)
        if(data_sum == num):
            return True
        elif(data_sum < num):
            start+=1
        else:
            end-=1
        data_sum = 0

    return False

if __name__ == '__main__':
    example = 13
    print(judgeSquareSum(example))
