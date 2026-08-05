# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # optimal solution -- using iterative stack
        # ---most accepted and recommended solution
        # important question -- google interview-- always explain that why iterative is better than reciursive----- say this:
        # iterative inorder traversal avoid recursion stack overhead and gives better control over the memory
# tc : o(n) --- sc : o(n)
        result = []
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result
# ---- recursive solution ---

        










