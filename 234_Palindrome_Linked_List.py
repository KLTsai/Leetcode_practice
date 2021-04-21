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

    def reverseAndClone(self, node):
        head = None
        while(node != None):
            n = ListNode(node.val)
            n.next = head
            head = n 
            node = node.next
        
        return head

    def isPalindrome(self, head, new):
        #to check every node that is same
        while (head!=None and new!=None):
            #print ("curr = ", curr.val)
            #print ("head = ", head.val)
            if (new.val != head.val): 
                return False
 
            new = new.next
            head = head.next
        
        return head == None and new == None

if __name__=="__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(1)

    test = LinkedList()
    test.add_node(node1)
    test.add_node(node2)
    test.add_node(node3)
    test.add_node(node4)

    chex = test.reverseAndClone(test.head)
    test.traversallist(chex)

    # new_list = test.reverseList(test.head)
    # test.traversallist(new_list)

    outcome = test.isPalindrome(test.head, chex)
    print("Result = ", outcome)