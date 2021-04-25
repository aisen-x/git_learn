from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        queue = [root]
        while queue:
            res.append([node.val for node in queue])
            lt = []
            for node in queue:
                if node.left:
                    lt.append(node.left)
                if node.right:
                    lt.append(node.right)
            queue = lt

        return res
