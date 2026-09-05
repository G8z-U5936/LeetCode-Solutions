# Definition for a binary tree node.
from collections import defaultdict, deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)
        queue = deque([root])
        while queue:
            node = queue.popleft()

            freq[node.val] += 1

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        max_frequency = max(freq.values())

        ans = []

        for value, frequency in freq.items():
            if frequency == max_frequency:
                ans.append(value)

        return ans