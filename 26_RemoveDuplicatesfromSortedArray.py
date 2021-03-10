#這題想法上關鍵input array (nums)已sorting
#建立set，可以知道那些元素(不重複)
#將set取代nums的矩陣，一個對一個，所以剩餘的元素為需要替除

if __name__ == '__main__':
    print("program entry")
    example = [0,0,1,1,1,2,2,3,3,4]
    num_set = sorted(set(example))

    print("set",num_set)


    for i, j in enumerate(num_set):
        example[i] = j

    print("modify example", example)
    
    for i in range(len(example)-len(num_set)):
        example.pop()
    print("outcome", example)