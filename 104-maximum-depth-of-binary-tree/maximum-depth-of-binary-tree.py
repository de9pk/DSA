# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([])
        h = 0
        q.append(root)
        while q:
            level_size = len(q)
            h+=1
            for _ in range(level_size):
                e = q.popleft()
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
        return h