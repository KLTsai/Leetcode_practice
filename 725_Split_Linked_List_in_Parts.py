'''
It's complicated for me when I think of it first time

Example 1:
Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]

Example 2:
Input: 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
'''
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

    def splitListToParts(self, root, k):
        dummy = ListNode(-1)
        dummy.next = root
        dummy = dummy.next
        cnt = 0 # 節點長度
        while (dummy):
            cnt += 1
            dummy = dummy.next
        
        part = cnt // k # 每一組含有多少elements
        remains = cnt % k # 餘數
        result = [None]*k
        
        # two pointers
        prev = None
        curr = root
        
        for i in range(len(result)):    
            n = 0
            result[i] = curr
            
            while (curr):
                prev = curr 
                curr = curr.next
                n += 1
                if(n - part == 1 and remains>0 and prev):
                    prev.next = None
                    remains-=1
                    break
                elif (n == part and remains<=0 and prev):
                    prev.next = None
                    break

        return result


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)


    test = LinkedList()
    test.add_node(node1)
    test.add_node(node2)
    test.add_node(node3)
    test.add_node(node4)
    test.add_node(node5)
    test.add_node(node6)
    test.add_node(node7)

    result_list = test.splitListToParts(test.head, 3)
