#class Solution:
#    def arrayPairSum(self, nums: List[int]) -> int:
def arrayPairSum(nums):
    #new_sort = []
    new_sort = sorted(nums) #first to sort ascending
    #length = len(new_sort)
    #minsum = 0
    
    #for idx in range(0, length, 2):
    #   minsum += new_sort[idx]
    return sum(new_sort[::2])

if __name__ == '__main__':
    print("program entry")
    checck = [6,2,6,5,1,2]
    outcome = arrayPairSum(checck)
    print(outcome)