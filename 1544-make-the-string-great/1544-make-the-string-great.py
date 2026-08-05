class Solution:
    def makeGood(self, s: str) -> str:
        # must write the base cases---------
        if len(s) == 1:
            return s
        if len(s) == 0:
            return ""
        stack = []

        for ch in s:
            if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
                stack.pop()
            else:
                stack.append(ch)
        
        return "".join(stack)


# tc : o(n) -> each char pushed and popped once
# sc : o(n) --- stack storage
