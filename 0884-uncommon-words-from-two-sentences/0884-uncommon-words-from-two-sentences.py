class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split() + s2.split()
        uncommon = []
        count = Counter(words)
        for key,value in count.items():
            if value == 1:
                uncommon.append(key)

        return uncommon
                