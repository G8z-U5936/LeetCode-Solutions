class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        last_op = "+"
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch in "+-*/" or i == len(s) - 1:
                if  last_op == "+":
                    stack.append(num)

                elif  last_op == "-":
                    stack.append(-num)
                    

                elif  last_op == "*":
                    stack.append(stack.pop() * num)
                    

                elif  last_op == "/":
                    stack.append(int(stack.pop() / num))
                
                num = 0
                last_op = ch
        
        return sum(stack)
