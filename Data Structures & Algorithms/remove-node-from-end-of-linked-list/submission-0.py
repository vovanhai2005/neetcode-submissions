# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0 , head)
        cur = dummy
        suf = head

        while n:
            suf = suf.next
            n -= 1
        
        while suf:
            cur = cur.next
            suf = suf.next

        tmp = cur.next
        cur.next = tmp.next

        return dummy.next

