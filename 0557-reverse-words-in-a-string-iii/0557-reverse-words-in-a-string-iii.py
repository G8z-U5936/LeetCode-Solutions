class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        for i in range(len(words)):
            word = list(words[i])
            # list are mutable.changes are allowed.
            left = 0
            right = len(word) - 1
            while left < right:
                word[left] , word[right] = word[right] , word[left]
                left += 1
                right -= 1
    # if i remove words[i] and if i directly write .join(words) then it wil;l not change anything.
    # bcoz .join creates a new reversed string . if u will  not store or assign it anywhere then it will thrown away.
            words[i] = "".join(word)

        return " ".join(words)
        

