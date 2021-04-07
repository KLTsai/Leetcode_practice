'''
Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: 
The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. 
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
----------------------------------------------------------------------------------------------------------------------

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: 
The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. 
There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
----------------------------------------------------------------------------------------------------------------------

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: 
From the head of A, it reads as [2,6,4]. 
From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

'''

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self, val)
        self.head = None
        self.tail = None
    
    def add_node(self, val)
        if not isinstance(val, ListNode):
            val = ListNode(val)

        if self.head == None:
            self.head = val
        else:
            self.tail.next = val
        
        self.tail = val

        return


def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None

    p = headA
    q = headB

    while p!=None and q!=None and p!=q:
        p = p.next
        q = q.next
        
        if p == q :
            return p
        if not p :
            p = headB
        if not q :
            q = headA
    
    return p


if __name__ == "__main__":
    test = ListNode(1)
    test2 = ListNode(1)
    result = getIntersectionNode(test, test2)
    print(result)
