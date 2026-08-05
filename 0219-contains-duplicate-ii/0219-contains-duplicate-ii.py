class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # n = len(nums)
        # for i in range(n):
        #     for j in range(1,n):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True
        # return False  


# hashset + dict ----> o(n) --- optimize solution 
        mydict = {}
        for idx,num in enumerate(nums):
            if num in mydict and abs(mydict[num] - idx) <= k:
                return True

            mydict[num] = idx
        
        return False


