#此題submission較多次，不清楚題目意義，需重新理解再試試


def findLongestWord (s, d):
    # 按照英字母顺序排序
    d = sorted(d)
    # 長度降序排序
    d = sorted(d, key=lambda x:len(x), reverse=True)
    # print(d)
    # lens = len(s)
    for word in d:
        lenw = len(word)
        #定义双指针
        lw = 0
        ls = 0 
        # 當ls移動的位數超過s的長度，則終止循環
        while ls <= len(s)-1:
            # 若字符相等，則lw指針向後移動一位
            if s[ls] == word[lw]:
                lw += 1
            # 無論何時，ls 指針總向後移動一位
            ls += 1
            if lw == lenw:
                #print(1)
                return word
    return ""

if __name__ == "__main__":
    s1 = "aewfafwafjlwajflwajflwafj"
    dictionary1 = ["apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf"]

    # dictionary1 = sorted(dictionary1)
    # dictionary1 = sorted(dictionary1, key=lambda x:len(x), reverse=True)
    result = find2(s1, dictionary1)
    # result = findLongestWord(s1, dictionary1)
    print(result)
