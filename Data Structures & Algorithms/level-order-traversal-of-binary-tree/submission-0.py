# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        res = []
        queue.append(root)

        while queue:
            cnt = len(queue)
            tmp = []
            
            for i in range(cnt):
                node = queue.popleft()
                if node:
                    tmp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if len(tmp):
                res.append(tmp)

        return res
        

         