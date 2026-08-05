class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(":
                stack.append(")")
            elif char == "{":
               stack.append("}") 
            elif char == "[":
               stack.append("]")
            else:
                if not stack or stack.pop() != char:
                    return  False

        return not stack

# space efficient optimal solution : both time and space complexity-- o(n) 
# parenthesis problen require remembering the previous problem -- no solution can work in o(1) space complexity for all rhe cases.

        stack = []
        mydict = {")":"(" , "}":"{" , "]":"["}
        for char in s:
            if char in mydict:
                popped_element = stack.pop() if stack else "#"
                if mydict[char] != popped_element:
                    return False
            else:
                stack.append(char)
        
        return not stack




