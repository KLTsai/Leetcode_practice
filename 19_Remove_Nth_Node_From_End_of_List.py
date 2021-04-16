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

    def removeNthFromEnd(self, head, n):
        cur = head
        i = 0

        # firstly, cur moves node to the end 
        while cur:
            i += 1
            cur = cur.next

        if (n == i): 
            ans = head
            ans = ans.next
            return ans

        pos = i - n # get position of what I want to remove
        cnt = 1

        dummy = head
        while dummy:
            if (cnt == pos):
                temp = dummy.next
                dummy.next = temp.next
            
            dummy = dummy.next
            cnt += 1
        
        return head


if __name__ == "__main__":
    
    test = Linkedlist()
    test.add_node(1)
    test.add_node(2)
    test.add_node(4)
    test.add_node(7)
    test.add_node(5)
    test.add_node(9)

    reNo = 3
    result = test.removeNthFromEnd(test.head, reNo)
    test.traversallist(result)

        
        





    