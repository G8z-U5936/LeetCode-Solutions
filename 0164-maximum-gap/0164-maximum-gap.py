class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse = True)
        result = []
        if n == 1:
            return 0
        for i in range(n-1):
            diff = nums[i] - nums[i+1]
            result.append(diff)

        return max(result)