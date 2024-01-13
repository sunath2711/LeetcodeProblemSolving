# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        def getLength(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        lenA, lenB = getLength(headA), getLength(headB)
        lastNodeA, lastNodeB = headA, headB
        
        while lastNodeA.next:
            lastNodeA = lastNodeA.next

        while lastNodeB.next:
            lastNodeB = lastNodeB.next
            
        if lastNodeA != lastNodeB:
            return None  
        
        longer = headA if lenA > lenB else headB
        shorter = headB if lenA > lenB else headA
        
        for _ in range(abs(lenA - lenB)):
            longer = longer.next
            
        while longer != shorter:
            longer = longer.next
            shorter = shorter.next

        return longer
