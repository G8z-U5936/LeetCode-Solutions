class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        clean = ""

        for ch in s:
            if ch.isalnum():
                clean += ch.lower()

        return clean == clean[::-1]
      
# clean[::-1] is the new string bcoz we can't modify the original string(clean)
            
            