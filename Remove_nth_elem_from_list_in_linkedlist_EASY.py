# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#important thing is to use two pointers
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        current = head
        current_plus_N = head
        
        for _ in range(n):
            current_plus_N = current_plus_N.next
        if current_plus_N is None:
            return head.next
        
        while current_plus_N.next is not None:
            current = current.next
            current_plus_N = current_plus_N.next
        current.next = current.next.next
        return head
        
            
            
        
