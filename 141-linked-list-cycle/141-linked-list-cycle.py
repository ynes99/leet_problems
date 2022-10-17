# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if (not head or not head.next):
            return False
        
        slow_ptr = head
        fast_ptr = head

        while (fast_ptr.next and fast_ptr.next.next):
            
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            
            if (slow_ptr == fast_ptr):
                return True
        return False