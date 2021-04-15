#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        return

class LinkedList:
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

        return
    
    def traversallist(self, head): 
        while(head!=None): 
            print (head.val) 
            head = head.next

    def reverseList(self, data):
        if not data:
                return head 
                
        pre = None
        cur = data
        prec = data.next

        while (prec!= None):
            cur.next = pre
            pre = cur 
            cur = prec
            prec = prec.next
            
        cur.next = pre
        
        return cur

if __name__ == "__main__":
    node1 = ListNode(5)
    node2 = ListNode(3)
    node3 = ListNode(1)
    node4 = ListNode(7)

    test = LinkedList()
    test.add_node(node1)
    test.add_node(node2)
    test.add_node(node3)
    test.add_node(node4)


    result = test.reverseList(node1)
    
    test.traversallist(result)


