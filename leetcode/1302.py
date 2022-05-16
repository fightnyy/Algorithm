# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        parent_node_list = [root]
        child_node_list = []
        sum_value = 0
        while parent_node_list:
            node = parent_node_list.pop(0)
            sum_value += node.val
            if node.left:
                child_node_list.append(node.left)
            if node.right:
                child_node_list.append(node.right)
            if not parent_node_list and child_node_list:
                parent_node_list = child_node_list[:]
                child_node_list.clear()
                sum_value = 0
            if not parent_node_list and not child_node_list:
                return sum_value
            
                
            
        