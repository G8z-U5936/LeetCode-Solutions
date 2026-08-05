class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        left = 0
        hashset = Counter(s1)
        prm = Counter
        k = len(s1)
        n = len(s2)
        window = Counter(s2[:k])
        if n < k:
            return False

        if window == hashset:
            return True
            
        for i in range(k,n):
            window[s2[i]] += 1
            window[s2[i - k]] -= 1
            if window[s2[i - k]] == 0:
                del window[s2[i - k]]
            
            if window == hashset:
                return True

        return False
        











