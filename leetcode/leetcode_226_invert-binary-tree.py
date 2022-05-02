# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = (
                self.invertTree(root.right),
                self.invertTree(root.left),
            )
            return root


# Definition for a binary tree node.
# class TreeNode:

#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        deque = collections.deque([root])
        while deque:
            tmp = deque.pop()

            if tmp:
                tmp.left, tmp.right = tmp.right, tmp.left

                deque.append(tmp.right)
                deque.append(tmp.left)

        return root
