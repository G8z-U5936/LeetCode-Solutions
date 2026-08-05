# 1st approach(not a better approach)
# from typing import List 
# from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = len(nums)
        majority = m//2
        count = defaultdict(int)
        for num in nums: 
            # count[num] += 1
            if count[num] > majority:
                return num








# t.c = o(n)
# s.c = o(n) (for both the solutions)            
        
# # 2nd approach
# from typing import List
# from collections import Counter 
# capital c in counter and small in collection
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = Counter(nums) 
#         return max(count,key =count.get )

# 3rd approach: sorting based approach 
# tc :   
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        # sorting will take o(n log n) time --- sc : o(1)
        return nums[len(nums)//2]
        #  floor division

# 4th approach: (better approach) : boyre-moore voting algo. 
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count == 0
#         candidate = None 
#         for num in nums:
#             if count == 0:
#                 candidate = num
#                 count = 1
#             elif candidate == num:
#                 count +=1
#             else:
#                 count -=1
#         return candidate        



        
