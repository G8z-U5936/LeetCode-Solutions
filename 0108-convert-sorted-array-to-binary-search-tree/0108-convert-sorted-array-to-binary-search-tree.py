# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        stack = [
            (root, 0, mid - 1, True),
            (root, mid + 1, len(nums) - 1, False)
        ]

        while stack:
            parent, left, right, is_left = stack.pop()

            if left > right:
                continue

            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            if is_left:
                parent.left = node
            else:
                parent.right = node

            stack.append((node, left, mid - 1, True))
            stack.append((node, mid + 1, right, False))

        return root
        

        


