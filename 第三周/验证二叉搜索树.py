class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 左中右遍历 最后遍历排序为升序
        res = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        return res == sorted(res) and len(set(res)) == len(res)
