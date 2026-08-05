class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # brute force--tc : o(n2) , sc: o(n)
        ans = []
        for i in range(len(nums1)):
            idx = nums2.index(nums1[i])
            found = False
            for j in range(idx + 1,len(nums2)):
                if nums2[j] > nums1[i]:
                    ans.append(nums2[j])
                    found = True
                    break
            if not found:
                ans.append(-1)

        return ans

# optimal solution (using stack) --- 
        














