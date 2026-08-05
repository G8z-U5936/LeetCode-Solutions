class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        lst = path.split("/")
        for ch in lst:
                if ch == "." or ch == "":
                    continue
                elif ch == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)

        return "/" + "/".join(stack)
        
                    
                
      
    


     