# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_ptr = head
        fast_ptr = head
        
        while fast_ptr and fast_ptr.next :
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next # double 
        return(slow_ptr)
    
    