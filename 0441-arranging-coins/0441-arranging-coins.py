class Solution:
    def arrangeCoins(self, n: int) -> int:
        hashset = set()
        if n == 1:
            return 1
        st = 1 
        ed = n
        while st < ed:
            mid = (st + ed) // 2
            needed = mid * (mid + 1) // 2
            if mid in hashset:
                return mid
            hashset.add(mid)

            if needed > n:
                ed = mid
            if needed < n:
                st = mid
            


        
            
        
                
            