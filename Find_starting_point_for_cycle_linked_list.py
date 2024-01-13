# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
            if slow == fast:
                break 
                
        else:
            return None         
                
        slow = head
    
        while slow != fast:
            slow = slow.next
            fast = fast.next
    
        return slow        

# after collision taks place, we assign slow= head and then .next for both fast adn slow till they are same, this gives us start of cycle.
