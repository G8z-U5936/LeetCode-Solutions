class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        j = 0
        idx = j - 1
        while j <= n-1 :
            if nums[j] % 2 == 0:
                idx += 1
                nums[idx],nums[j] = nums[j],nums[idx]
            j += 1
            
        return nums 