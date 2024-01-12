# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# # Return true if there is a cycle in the linked list. Otherwise, return false.
# Here's a simple algorithm to check for a cycle in a linked list, commonly known as Floyd's Tortoise and Hare algorithm:

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head is None or head.next is None:
            return False
        
        tortoise = head
        rabbit = tortoise.next
            
        while tortoise != rabbit:
            if rabbit is None or rabbit.next is None:
                return False
            tortoise= tortoise.next
            rabbit= rabbit.next.next
        
        return True    

# the logic is simple, we wish to find if there is a cycle in the linkedlist. so we take w pointers one slow other fast
# slow takes one jump fast takes two jumps, if the fast one reaches end before slow, there is no cycle, but if there is a cycle slow and fast will meet at an index.
# this way we can identify there is a cycle or not
# Also called floyds tortiose or hare algo
