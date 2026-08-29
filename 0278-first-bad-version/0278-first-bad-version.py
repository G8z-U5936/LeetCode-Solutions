# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        st = 1
        ed = n
        while st < ed:
            mid = (st + ed) // 2

            if isBadVersion(mid):
                ed = mid
                
            else:
                st = mid + 1
        
        return st