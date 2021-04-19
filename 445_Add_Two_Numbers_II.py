'''
Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, val):
        if not isinstance(val, ListNode):
            val = ListNode(val)
        
        if self.head is None:
            self.head = val
        else:
            self.tail.next = val

        self.tail = val

    def traversallist(self, head):
        while (head):
            print (head.val)
            head = head.next 

    def addTwoNumbers (self, L1, L2):
        dummy = ListNode(-1)
        stack1, stack2 = [], []
        
        def pushback(nodes):
            s = []
            while (nodes):
                s.append(nodes.val)
                nodes = nodes.next
            return s

        stack1 = pushback(L1)
        stack2 = pushback(L2)

        carry = 0

        while stack1 or stack2 or carry :
            tmp1, tmp2 = 0, 0
            if (stack1):
                tmp1 = stack1.pop()
            if (stack2):
                tmp2 = stack2.pop()

            div = (tmp1 + tmp2 + carry) // 10 #商數
            mod = (tmp1 + tmp2 + carry) % 10 #餘數
            carry = div #進位

            #push front (想成一組Linkedlist插入一顆新的Node) 
            curr = ListNode(mod) #建立新節點
            curr.next = dummy.next
            dummy.next  = curr

        return dummy.next

if __name__== "__main__":

    test = Linkedlist()
    test.add_node(3)
    test.add_node(2)
    test.add_node(4)
    test.add_node(3)
    
    test2 = Linkedlist()
    test2.add_node(7)
    test2.add_node(3)
    test2.add_node(4)
    test2.add_node(1)

    result = test.addTwoNumbers(test.head, test2.head)
    test.traversallist(result)
