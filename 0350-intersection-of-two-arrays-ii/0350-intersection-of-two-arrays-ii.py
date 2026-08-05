from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_count = Counter(nums1)
        result = []

        for num in nums2:
            if num in num1_count and num1_count[num]>0:
                result.append(num)
                num1_count[num] -= 1

        return result

# using hashset:



