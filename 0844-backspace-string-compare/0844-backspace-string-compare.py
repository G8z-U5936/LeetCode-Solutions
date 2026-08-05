class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for ch in s:
            if ch == "#" and stack1:
                stack1.pop()
            elif ch != "#":
                stack1.append(ch)

        for ch in t:
            if ch == "#" and stack2:
                stack2.pop()
# dont use else bcoz if stack is empty then else runs and  # gets appended in stack which is wrong . it should never be in the stack
            if ch != "#":
            # you can either use elif or if condition not else.
                stack2.append(ch)

        return stack1 == stack2

# using two stack------- will work correctly
# tc : o(n + m)
# sc : o(n + m)

# using two pointer approach---- optimal
# tc : o(n + m)
# sc : o(1) --- constant space




