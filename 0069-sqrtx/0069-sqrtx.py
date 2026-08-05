class Solution:
    def mySqrt(self, x: int) -> int:
        hashset = set()
        if x < 2:
            return x
        left = 1
        right = x
        while left < right:
            mid = (left + right) // 2
            sq = mid * mid

            if mid in hashset:
                return mid
            hashset.add(mid)

            if sq > x:
                right = mid
            else:
                left = mid
            


                  

