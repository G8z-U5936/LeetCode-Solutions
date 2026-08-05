class Solution:
    def firstUniqChar(self, s: str) -> int:
        mydict = {}
        for num in s:
            mydict[num] = mydict.get(num,0) + 1
        for idx,num in enumerate(s):
            if mydict[num] == 1:
                return idx
        
        return -1
            


            
