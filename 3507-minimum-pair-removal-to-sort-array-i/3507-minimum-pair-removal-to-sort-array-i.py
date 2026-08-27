class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # default behaviour of sorted --> ascending order
        operations = 0

        while nums != sorted(nums):
            min_sum = float('inf')

            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < min_sum:
                    min_sum = nums[i] + nums[i + 1]
                    index = i

            nums[index] = nums[index] + nums[index + 1]
            nums.pop(index + 1)

            operations += 1

        return operations