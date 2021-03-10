'''
Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
'''
if __name__ == '__main__':
# use two pointer conception
    numbers = [5,25,75]
    target = 100
   
    start = 0
    end = len(numbers)-1
    
    output = []

    while start < end:
        if((numbers[start] + numbers[end]) == target):
            output.append([start+1, end+1])
            break
        elif ((numbers[start] + numbers[end]) < target):
            start+=1
        else:
            end-=1

    print(output)

    '''
    for q, p in enumerate(numbers):
        output[0] = q+1
        start = p
        for k in range(len(numbers)-1,-1,-1):
            end = numbers[k]
            sum_ele = start + end

            if (sum_ele == target):
                output.append(k+1)
    '''