class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for ch in logs:
            if ch == "../":
                if depth > 0:
                    depth -= 1 
            
            elif ch == "./" :
                pass
            
            elif ch == "x/":
                depth += 1 
            
            else:
                depth += 1 

        return depth










