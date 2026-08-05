# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # -----------------preorder dfs-----------------------
        if not root:
            return False
        stack = [(root, root.val)]
        
        while stack:
            node, currsum = stack.pop()
            if not node.left and not node.right:
                if currsum == targetSum:
                    return True


            if node.left:
                stack.append((node.left, currsum + node.left.val))

            if node.right:
                stack.append((node.right, currsum + node.right.val))

        return False