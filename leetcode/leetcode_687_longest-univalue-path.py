# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        result = 0

        def _dfs(root):
            node = root
            if node == None:
                return 0

            left = _dfs(node.left)
            right = _dfs(node.right)

            if node.left and node.val == node.left.val:
                left += 1
            else:
                left = 0
            if node.right and node.val == node.right.val:
                right += 1

            else:
                right = 0
            nonlocal result
            result = max(result, left + right)

            return max(left, right)

        _dfs(root)
        return result
