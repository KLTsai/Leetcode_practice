'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

 

Example 1:

Input: s = "hello"
Output: "holle"
------------------------------------------------------

Example 2:
Input: s = "leetcode"
Output: "leotcede"

'''
#雙指針搜尋 很好範例
if __name__ == "__main__":
    s = "aA"
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = list(s)
    fwrdidx = 0
    backidx = len(s)-1
    
    while fwrdidx < backidx:
        
        if string[fwrdidx].lower() not in vowels:
            fwrdidx += 1
        elif string[backidx].lower() not in vowels:
            backidx -= 1
        else: #swap
            temp = string[fwrdidx]
            string[fwrdidx] = string[backidx]
            string[backidx] = temp
            fwrdidx += 1
            backidx -= 1

    print("".join(string))
