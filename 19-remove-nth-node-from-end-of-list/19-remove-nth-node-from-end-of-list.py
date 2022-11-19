# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        index = 0
        dummy = count = head
        len_list = 0
        
        while count :
            count = count.next
            len_list +=1
        target = len_list - n - 1
        print(target)
        if target == -1:
            return(head.next)
        while head :
            if index == target :
                tmp = head.next.next
                head.next = tmp
                break
            head = head.next
            index += 1
        return(dummy)
            