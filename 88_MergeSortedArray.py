
if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    start = 0
    for q, p in enumerate(nums1):
        if q >= m:
            nums1[q] = nums2[start]
            start+=1
    
    nums1.sort()
    print(nums1)