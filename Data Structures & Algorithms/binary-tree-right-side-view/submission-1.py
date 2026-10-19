# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        dic = {}

        def helper(level, node):
            if not node:
                return
            helper(level + 1, node.left)
            helper(level + 1, node.right)
            dic[level] = node.val

        helper(0, root)
        res = []
        keys = sorted(dic.keys())
        for k in keys:
            res.append(dic[k])
        return res
        