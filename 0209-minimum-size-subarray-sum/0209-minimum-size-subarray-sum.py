class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        minimum = float('inf')
        left = 0
        sm = 0
        
        for right in range(n):
            sm += nums[right]

            while sm >= target:
                minimum = min(minimum, right - left + 1)
                sm -= nums[left]
                left += 1

        return 0 if minimum == float("inf") else minimum






                                                                                                                              