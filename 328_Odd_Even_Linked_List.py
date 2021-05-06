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

    def oddEvenList(self, head):
    
    #          1    2    3    4    5    6    7
                  
    #         (1)->(3)->(2)->(4)->(5)->(6)->(7)->NULL
    # curr                         ^     
    # oddH     ^
    # oddT          ^
    # evenH              ^
    # evenT                   ^


    #          1    2    3    4    5    6    7
                       
    #         (1)->(3)->(5)->(2)->(4)->(6)->(7)->NULL
    # curr                                   ^               
    # oddH     ^
    # oddT               ^
    # evenH                   ^
    # evenT                             ^
    

        if (head == None or head.next == None or head.next.next == None):
            return head


        oddHead = head
        oddTail = head
        evenHead = head.next
        evenTail = head.next
        curr = evenTail.next

        #start to move
        while (curr):
            oddTail.next = curr
            evenTail.next = curr.next
            curr.next = evenHead
            
            oddTail = curr
            evenTail = evenTail.next
            if (evenTail == None):
                break
            curr = evenTail.next
            
        return oddHead

    

if __name__== "__main__":
    
    test = Linkedlist()
    test.add_node(1)
    test.add_node(2)
    test.add_node(3)
    test.add_node(4)
    test.add_node(5)
    test.add_node(6)
    test.add_node(7)

    result = test.oddEvenList(test.head)

    test.traversallist(result)