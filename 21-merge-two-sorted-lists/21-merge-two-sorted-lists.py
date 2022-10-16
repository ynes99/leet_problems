# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
         
        head = cur = ListNode() #cursor for the final listNode
        while list1 and list2 : #list1 and list 2 != None
            if list1.val >= list2.val:
                cur.next = list2
                list2 = list2.next
                
            else:
                cur.next = list1
                list1 = list1.next
            cur = cur.next
        if list1: #if list2 ends and list1 still has elements we append them to the cursor
            cur.next = list1
        if list2:
            cur.next = list2
        return(head.next)