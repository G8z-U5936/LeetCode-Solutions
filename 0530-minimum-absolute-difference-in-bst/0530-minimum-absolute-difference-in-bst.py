# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        arr = []

        while stack:
            node = stack.pop()

            if node:
                arr.append(node.val)

                if node.left:
                    stack.append(node.left)

                if node.right:
                    stack.append(node.right)

        arr.sort()

        min_diff = float('inf')

        for i in range(1, len(arr)):
            min_diff = min(min_diff, abs(arr[i] - arr[i - 1]))

        return min_diff