class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mydict = {}
        intersection = []

        for num in nums1:
            mydict[num] = mydict.get(num,0) + 1

        for num in nums2:
            if num in mydict and mydict[num] > 0:
                intersection.append(num)
                mydict[num] -= 1

        return list(set(intersection))