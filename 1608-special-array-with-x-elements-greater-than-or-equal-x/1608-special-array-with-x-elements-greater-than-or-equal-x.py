class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0,n+1):
            j = 0
            count = 0
            while j < n:
                if nums[j] >= i:
                    count += 1
                j += 1
            if count == i:
                print(count)
                return i

        return -1
                 
