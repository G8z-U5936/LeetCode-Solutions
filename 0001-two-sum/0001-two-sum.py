class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # brute force -- o(n2)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] + nums[j] == target:
        #             return i,j


        # optimize sol.---- tc o(n)
        seen = {}
        for idx,num in enumerate(nums):
            find = target - num
            if find in seen:
                return[seen[find] , idx]
            
            seen[num] = idx
        
        return []


