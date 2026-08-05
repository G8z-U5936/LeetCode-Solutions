# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result



    # class Solution:-----explanation
    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
    #     def recur(node):
    #         if node == None:
    #             return []
            
    #         # print(node.val, "->", end="")
    #         curr_list = [node.val]
    #         left_list = recur(node.left)
    #         right_list = recur(node.right)

    #         return curr_list + left_list + right_list

    #     return recur(root)