# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Node:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        res = ListNode(0)
        cur = res
        minHeap = []

        for singleList in lists:
            if singleList is not None:
                heapq.heappush(minHeap, Node(singleList))
        
        while minHeap:
            tmp = heapq.heappop(minHeap)
            cur.next = tmp.node
            cur = cur.next

            if tmp.node.next:
                heapq.heappush(minHeap, Node(tmp.node.next))
        
        return res.next
        