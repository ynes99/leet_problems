# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if(not head or not head.next):
            return False
			
		#Initializing slow and fast pointers
        slow = head
        fast = head 
		
		#Moving slow ptr at one step a time and fast ptr at two step at a time
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
			
			#If they meet then cycle is present for sure
            if(slow == fast):
                return True
        return False