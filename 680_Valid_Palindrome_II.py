
def validPalindrome(str):
    i = 0        #forward
    j = len(s)-1 #backward
    string = list(s)
    cnt = 0
    
    def is_Palindrome(r, l):
        while r < l:
            if(string[r] != string[l]): return False
            r+=1
            l-=1
        return True
    
    while i < j:
        if (string[i] != string[j]):
            return (is_Palindrome(i+1, j) or is_Palindrome(i, j-1))
                
        i += 1
        j -= 1

    return True



if __name__ == '__main__' :
    s = "cbbcc"
    result = validPalindrome(s)
    print(result)