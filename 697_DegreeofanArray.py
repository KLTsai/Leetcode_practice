
from collections import defaultdict
def findShortestSubArray(nums):
    
    element_dict = defaultdict(list)
    # find out the max freq length
    max_freq = 0
    short_path = float("inf") # 正無窮大 positive infinity
    short_n = 0

    for idx, val in enumerate(nums):
        element_dict[val].append(idx)
        length = len(element_dict[val]) 
        if(length > max_freq):
            max_freq = length
    
    #check short path
    for k, v in element_dict.items():
        if len(v) == max_freq:
            start = v[0]
            end = v[-1]
            diff = end - start + 1 # we know how many elements in "nums" when it exist short path.
            if (diff < short_path):
                short_path = diff
                
    return short_path


if __name__ == '__main__':
    check = [1,2,2,3,1,4,2]
    outcome = findShortestSubArray(check)
    print(outcome)