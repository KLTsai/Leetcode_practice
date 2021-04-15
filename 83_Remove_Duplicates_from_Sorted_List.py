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

    def removeDup(self, head):
        if not head: return None
        else:
            dummy = ListNode("-inf")
            tail = dummy
            
            while (head != None):
                if (head.val != tail.val):
                    tail.next = head
                    head = head.next
                    tail = tail.next
                    tail.next = None
                else:
                    head = head.next

        return dummy.next

if __name__ == "__main__":
    node1 = ListNode(0)
    node2 = ListNode(0)
    node3 = ListNode(0)
    node4 = ListNode(0)
    node5 = ListNode(0)
    node6 = ListNode(0)

    test = LinkedList()
    test.add_node(node1)
    test.add_node(node2)
    test.add_node(node3)
    test.add_node(node4)
    test.add_node(node5)
    test.add_node(node6)


    result = test.removeDup(node1)
    test.traversallist(result)