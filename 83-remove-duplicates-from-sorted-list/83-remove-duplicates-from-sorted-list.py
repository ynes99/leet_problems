# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        while head :
            while head.next :
                if head.val == head.next.val :
                    head.next = head.next.next
                else:
                    break
            head = head.next
            print(head)
        return dummy
            