from collections import Counter
def intersect(nums1, nums2):
    num1_ = sorted(nums1)
    num2_ = sorted(nums2)
    
    if(len(num1_) > len(num2_)):
        new_set = num1_
        tmp_set = num2_
    else:
        new_set = num2_
        tmp_set = num1_      
    
    output = []
    
    for i, j in enumerate(new_set):
        for m, n in enumerate(tmp_set):
            if(new_set[i] == tmp_set[m]):
                output.append(j)
                tmp_set.pop(m)
                break
    
    #下次review需要寫出效能家的寫法, hint = use Counter & map



    return output

if __name__ == '__main__':
    example = [1,2,3,4,5,6,7,8]
    ex2 = [5,4,3,2,1,1]
    output = intersect(example, ex2)
    print(output)