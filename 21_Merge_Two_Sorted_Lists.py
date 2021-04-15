#Linkedlist merge
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

    def mergeTwolists(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        
        
        while (l1 and l2):
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next
             
        if(l1): tail.next = l1
        if(l2): tail.next = l2
        
        return dummy.next
        
#recursive        
#         if not l1: return l2
#         if not l2: return l1
        
#         if l1.val < l2.val:
#             l1.next = self.mergeTwoLists(l1.next, l2)
#             return l1
#         else:
#             l2.next = self.mergeTwoLists(l1, l2.next)
#             return l2


if __name__ == "__main__":

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)

    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)

    test = LinkedList()
    test.add_node(node1)
    test.add_node(node2)
    test.add_node(node3)

    test_2 = LinkedList()
    test_2.add_node(node4)
    test_2.add_node(node5)
    test_2.add_node(node6)

    result = test.mergeTwolists(node1, test_2.head)

    test.traversallist(result)