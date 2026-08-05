# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # official recursive solution -- most common --clean and easy to explain.
        # official two stack iterative solutioin -- no last visited , often recommended for interviews .
        # official one stack iterative solution(advanced) -- uses one stack , space optimal and in addition to this it demonstrate strong algorithmic control
        # remember they can ask to you  to explain all these approaches.
        #  remember you must have the knowledge of all of these approaches.

# first appproach -- iterative using one stack.
        
        result = []
        stack = []
        last_visited  = None
        current = root
        
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                peek = stack[-1]
                if peek.right and last_visited != peek.right:
                    current = peek.right
                else:
                    result.append(peek.val)
                    last_visited = stack.pop()

        return result

