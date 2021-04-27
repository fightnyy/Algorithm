# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 상태값 = 가장 말단(leaf node) 에서부터 현재 자신까지의 거리
        # 거리 = 현재노드 기준으로 left와 right의 상태값 +2 왜냐하면
        """
         q
        / \
       b   c
        """
        # 라고 할때 \가 2개 있는데 이를 거리라고 이해
        longest = 0

        def _dfs(node):
            if node == None:
                return -1

            left = _dfs(node.left)
            right = _dfs(node.right)

            nonlocal longest
            longest = max(
                longest, left + right + 2
            )  # 거리 longest와 left+right+2 중에 큰것 만약 그냥 left+right+2만 한다면 1-3일때 전혀 크지 않은데 갱신됨

            return max(left, right) + 1  # right와 left중에 하나가 더 큰 값이 더 긴 리프를 같고 있다

        _dfs(root)
        return longest
