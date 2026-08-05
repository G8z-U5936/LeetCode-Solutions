class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t
        count_s = Counter(s)
        count_t = Counter(t)
        for ch in t:
            if ch not in count_s or count_t[ch] != count_s[ch]:
                return ch
