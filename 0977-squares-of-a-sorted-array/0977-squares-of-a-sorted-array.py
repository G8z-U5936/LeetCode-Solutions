class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            a = num * num
            res.append(a)

        res.sort()
        return res
