"""
BFS = queue
DFS = Recursive or stack
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        answer = 0
        while queue:
            answer += 1
            for _ in range(len(queue)):
                Node = queue.popleft()
                if Node.left:
                    queue.append(Node.left)
                if Node.right:
                    queue.append(Node.right)

        return answer
