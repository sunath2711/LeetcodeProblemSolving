class ListNode:
    
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
        
    

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        
    
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or self.head is None:
            return -1

        current = self.head
        for _ in range(index):
            if current.next is None:
                return -1
            current = current.next

        return current.val
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = ListNode(val)
        node.next = self.head
        self.head = node
        
    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            return
            
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node    
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index <= 0:
            self.addAtHead(val)
            return

        new_node = ListNode(val)
        current = self.head

        for _ in range(index - 1):
            if current is None:
                return
            current = current.next

        if current is None:
            return

        new_node.next = current.next
        current.next = new_node
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return
        
        current = self.head
        for i in range(index-1):
            if current is None or current.next is None:
                return current
            current = current.next
            
        if current.next is not None:
            current.next = current.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
