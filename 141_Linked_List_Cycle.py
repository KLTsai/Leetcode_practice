
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Input: head = [3,2,0,-4], pos = 1
# output = True

# Input: head = [1,2], pos = 0
# output = True

# Input: head = [1], pos = -1
# output = False


# there is a cycle that includes 2 nodes at least.
if __name__ == "__main__":
    
    if(head == None): return False
    
    first = head
    second = head.next
    
    while (first != None and second != None and second.next != None ):
        
        if (first == second):
            print("output = ", True)
            break
        
        first = first.next
        second = second.next.next
    
    print("output = ", False)